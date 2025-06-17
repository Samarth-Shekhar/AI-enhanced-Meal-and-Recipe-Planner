import random
from data import food_items_breakfast, food_items_lunch, food_items_dinner

# Safe choice with fallback and calorie fix
def safe_random_choice(data_dict, group_name):
    items = list(data_dict.get(group_name, {}).keys())
    if not items:
        return f"No {group_name} item available", 0
    item = random.choice(items)
    calories = data_dict[group_name][item].get("calories", 0)
    return item, calories

# Breakfast Recipe Generator
def generate_breakfast_recipe(data):
    protein, c1 = safe_random_choice(data, "protein")
    whole_grain, c2 = safe_random_choice(data, "whole_grains")
    fruit, c3 = safe_random_choice(data, "fruits")
    fat, c4 = safe_random_choice(data, "healthy_fats")

    calories = c1 + c2 + c3 + c4
    instructions = f"Cook or prepare {protein}. Toast or cook {whole_grain}. Add fresh {fruit} and a serving of {fat}."

    recipe = {
        "Protein": protein,
        "Whole Grain": whole_grain,
        "Fruit": fruit,
        "Healthy Fat": fat,
        "Calories": calories,
        "Instructions": instructions
    }
    return recipe

# Lunch Recipe Generator
def generate_lunch_recipe(data):
    protein, c1 = safe_random_choice(data, "protein")
    grain, c2 = safe_random_choice(data, "whole_grains")
    vegetable, c3 = safe_random_choice(data, "vegetables")
    legume, c4 = safe_random_choice(data, "legumes")
    fat, c5 = safe_random_choice(data, "healthy_fats")

    calories = c1 + c2 + c3 + c4 + c5
    instructions = (
        f"Grill or cook {protein}. Prepare {grain} as a side. Add steamed or raw {vegetable}, "
        f"include {legume} for extra protein. Drizzle with {fat}."
    )

    recipe = {
        "Protein": protein,
        "Grain": grain,
        "Vegetable": vegetable,
        "Legume": legume,
        "Healthy Fat": fat,
        "Calories": calories,
        "Instructions": instructions
    }
    return recipe

# Dinner Recipe Generator
def generate_dinner_recipe(data):
    protein, c1 = safe_random_choice(data, "proteins")
    grain, c2 = safe_random_choice(data, "grains_and_starches")
    vegetable, c3 = safe_random_choice(data, "vegetables")
    sauce, c4 = safe_random_choice(data, "sauces_and_condiments")
    fat, c5 = safe_random_choice(data, "healthy_fats")

    calories = c1 + c2 + c3 + c4 + c5
    instructions = (
        f"Cook {protein} and prepare {grain}. Steam or roast {vegetable}. "
        f"Add {sauce} for flavor and serve with a side of {fat}."
    )

    recipe = {
        "Protein": protein,
        "Grain": grain,
        "Vegetable": vegetable,
        "Sauce": sauce,
        "Healthy Fat": fat,
        "Calories": calories,
        "Instructions": instructions
    }
    return recipe

# Optional CLI test
def print_recipe(meal_name, recipe):
    print(f"\n--- {meal_name} Recipe ---")
    for key, value in recipe.items():
        print(f"{key}: {value}")

def main():
    print("🍽️ Testing AI Meal Recipes")

    breakfast = generate_breakfast_recipe(food_items_breakfast)
    print_recipe("Breakfast", breakfast)

    lunch = generate_lunch_recipe(food_items_lunch)
    print_recipe("Lunch", lunch)

    dinner = generate_dinner_recipe(food_items_dinner)
    print_recipe("Dinner", dinner)

if __name__ == "__main__":
    main()

