

# 🧠 AI Meal Planner App 🍽️

The **AI Meal Planner** is a smart dietary planning application that creates personalized meal plans based on your age, weight, gender, and dietary preference (vegan, vegetarian, non-vegetarian). It calculates your BMR, optimizes meals using the knapsack algorithm, and generates creative descriptions using **LLaMA 3 (Groq API)**.

---

## 📸 Demo

### 🏠 Home Page  
![Home](assets/screenshots/ai_meal_1.png)

### 🧠 Meal Suggestions  
![Suggestions](assets/screenshots/ai_meal_2.png)

### 📝 Generated Meal Plan  
![Plan](assets/screenshots/ai_meal_3.png)

### 📄 PDF Export  
![PDF](assets/screenshots/ai_meal_4.png)

---

## 🔥 Features

- 🔢 BMR (Calorie) calculation based on user profile
- 🥦 Choose your diet: **Vegan**, **Vegetarian**, or **Non-Vegetarian**
- 📦 Meal optimization using **Knapsack algorithm**
- 🧠 AI-generated meal names and descriptions via **Groq’s LLaMA-3**
- 📄 Export full meal plan as a downloadable PDF
- 🧪 Streamlit-based interactive UI

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI & interactivity
- **Pandas** – Data manipulation
- **FPDF** – PDF export
- **Groq API** – AI-generated meal names & descriptions
- **Knapsack Algorithm** – Optimized food item selection

---

2. Add your Groq API key
Create a file .streamlit/secrets.toml and add:

toml
Copy
Edit
GROQ_API_KEY = "your_api_key"
3. Run the app
bash
Copy
Edit
streamlit run streamlit_meal_planner.py

📁 Project Structure
bash
Copy
Edit
AI-Meal-Planner/
│
├── data.py                   # Meal item data
├── knapsack.py               # Knapsack logic
├── pdf_exporter.py           # PDF export functionality
├── streamlit_meal_planner.py # Main Streamlit app
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml

👨‍💻 Author
Made with ❤️ by Samarth Shekhar
GitHub • LinkedIn

