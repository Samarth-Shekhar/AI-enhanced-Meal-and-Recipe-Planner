import streamlit as st
import pandas as pd
import requests
import random
import urllib3
from pdf_exporter import create_meal_plan_pdf

from data import (
    food_items_breakfast,
    food_items_lunch,
    food_items_dinner
)
from prompts import (
    pre_prompt_b, pre_prompt_l, pre_prompt_d,
    pre_breakfast, pre_lunch, pre_dinner,
    end_text, example_response_l, example_response_d, negative_prompt
)
from recipe_generator import (
    generate_breakfast_recipe,
    generate_lunch_recipe,
    generate_dinner_recipe
)

# Constants
UNITS_CM_TO_IN = 0.393701
UNITS_KG_TO_LB = 2.20462
UNITS_LB_TO_KG = 1 / UNITS_KG_TO_LB
UNITS_IN_TO_CM = 1 / UNITS_CM_TO_IN

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Groq API
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
    "Content-Type": "application/json"
}

# Page Setup
st.set_page_config(page_title="AI - Meal Planner", page_icon="🍴")
st.title("🍴 AI Meal Planner with Recipes & Descriptions")
st.divider()
st.markdown("*Powered by Groq (LLaMA-3)*")
st.divider()

# User Input
st.subheader("👤 Your Information:")
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", step=1)

unit_preference = st.radio("Preferred units:", ["Metric (kg, cm)", "Imperial (lb, ft + in)"])
if unit_preference == "Metric (kg, cm)":
    weight = st.number_input("Enter your weight (kg)")
    height = st.number_input("Enter your height (cm)")
else:
    weight_lb = st.number_input("Enter your weight (lb)")
    col1, col2 = st.columns(2)
    with col1:
        height_ft = st.number_input("Enter your height (ft)")
    with col2:
        height_in = st.number_input("Enter your height (in)")
    weight = weight_lb * UNITS_LB_TO_KG
    height = (height_ft * 12 + height_in) * UNITS_IN_TO_CM

gender = st.radio("Gender:", ["Male", "Female"])
diet = st.selectbox("Diet Preference", ["Vegan", "Vegetarian", "Non-Vegetarian"])

# BMR Calculation
def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        return 9.99 * weight + 6.25 * height - 4.92 * age + 5
    else:
        return 9.99 * weight + 6.25 * height - 4.92 * age - 161

bmr = calculate_bmr(weight, height, age, gender)
round_bmr = round(bmr, 2)
st.subheader(f"🍽️ Your Daily Requirement: **{round_bmr} Calories**")

# Diet Mapping
diet_map = {
    "Vegan": ["vegan"],
    "Vegetarian": ["vegan", "vegetarian"],
    "Non-Vegetarian": ["vegan", "vegetarian", "non-vegetarian"]
}

# Filter food items by diet
def filter_diet(food_data, allowed_types):
    return {
        group: {
            item: info for item, info in foods.items()
            if info.get("type", "non-vegetarian") in allowed_types
        }
        for group, foods in food_data.items()
    }

# Flatten for calories
def flatten_food_groups(food_groups):
    return {
        group: {
            item: info["calories"] for item, info in foods.items()
        } for group, foods in food_groups.items()
    }

# Knapsack calorie optimizer
def knapsack(target_calories, food_groups):
    items = [(cal, item) for group in food_groups.values() for item, cal in group.items()]
    n = len(items)
    if n == 0:
        return [], 0
    dp = [[0] * (target_calories + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(target_calories + 1):
            cal, _ = items[i - 1]
            if cal > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cal] + cal)
    selected_items = []
    j = target_calories
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            cal, item = items[i - 1]
            selected_items.append(item)
            j -= cal
    return selected_items, dp[n][target_calories]

# LLM description generator
def generate_meal_description(meal_items, pre_prompt, pre_meal):
    content = pre_prompt + str(meal_items) + pre_meal + negative_prompt
    response = requests.post(
        GROQ_API_URL,
        headers=HEADERS,
        json={"model": "llama3-70b-8192", "messages": [{"role": "user", "content": content}]},
        verify=False
    )
    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ LLM Error: {response.json().get('error', {}).get('message', str(e))}"

# Trigger Button
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button("Create Meal Basket", on_click=click_button)

# If clicked, generate meals
if st.session_state.clicked:
    calories_breakfast = round(bmr * 0.5)
    calories_lunch = round(bmr * 1/3)
    calories_dinner = round(bmr * 1/6)

    allowed_types = diet_map[diet]

    b_items = filter_diet(food_items_breakfast, allowed_types)
    l_items = filter_diet(food_items_lunch, allowed_types)
    d_items = filter_diet(food_items_dinner, allowed_types)

    b_items_flat = flatten_food_groups(b_items)
    l_items_flat = flatten_food_groups(l_items)
    d_items_flat = flatten_food_groups(d_items)

    meal_items_morning, cal_m = knapsack(calories_breakfast, b_items_flat)
    meal_items_lunch, cal_l = knapsack(calories_lunch, l_items_flat)
    meal_items_dinner, cal_d = knapsack(calories_dinner, d_items_flat)

    st.header("📦 Meal Basket")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(f"Calories: {calories_breakfast}")
        st.dataframe(pd.DataFrame({"Breakfast Items": meal_items_morning}))
        st.write(f"Total: {cal_m}")

    with col2:
        st.write(f"Calories: {calories_lunch}")
        st.dataframe(pd.DataFrame({"Lunch Items": meal_items_lunch}))
        st.write(f"Total: {cal_l}")

    with col3:
        st.write(f"Calories: {calories_dinner}")
        st.dataframe(pd.DataFrame({"Dinner Items": meal_items_dinner}))
        st.write(f"Total: {cal_d}")

    if st.button("Generate Recipes and Descriptions"):
        breakfast_recipe = generate_breakfast_recipe(b_items)
        lunch_recipe = generate_lunch_recipe(l_items)
        dinner_recipe = generate_dinner_recipe(d_items)

        desc_b = generate_meal_description(meal_items_morning, pre_prompt_b, pre_breakfast)
        desc_l = generate_meal_description(meal_items_lunch, pre_prompt_l, pre_lunch)
        desc_d = generate_meal_description(meal_items_dinner, pre_prompt_d, pre_dinner)

        for title, recipe, desc in zip(["Breakfast", "Lunch", "Dinner"],
                                       [breakfast_recipe, lunch_recipe, dinner_recipe],
                                       [desc_b, desc_l, desc_d]):
            st.markdown(f"## 🍱 {title}")
            st.markdown("### 📖 AI Description")
            st.write(desc)
            st.markdown("### 🧑‍🍳 Recipe Instructions")
            st.json(recipe)

        # Build meal data list
        meals_data = [
            {
                "title": "Breakfast",
                "calories": calories_breakfast,
                "items": meal_items_morning,
                "description": desc_b,
                "recipe": breakfast_recipe
            },
            {
                "title": "Lunch",
                "calories": calories_lunch,
                "items": meal_items_lunch,
                "description": desc_l,
                "recipe": lunch_recipe
            },
            {
                "title": "Dinner",
                "calories": calories_dinner,
                "items": meal_items_dinner,
                "description": desc_d,
                "recipe": dinner_recipe
            },
        ]

        user_info = {
            "name": name,
            "age": age,
            "gender": gender,
            "diet": diet,
            "bmr": round_bmr
        }

        pdf_filename = "meal_plan.pdf"
        create_meal_plan_pdf(meals_data, user_info, pdf_filename)

        with open(pdf_filename, "rb") as f:
            st.download_button(
                label="📥 Download Meal Plan as PDF",
                data=f,
                file_name=pdf_filename,
                mime="application/pdf"
            )

        st.success("✅ Recipes and meal descriptions generated successfully!")
