from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font('Arial', '', 12)
        self.add_page()

    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'AI-Powered Meal Plan', ln=True, align='C')
        self.ln(10)

    def user_info(self, user_data):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f"Name: {user_data['name']}", ln=True)
        self.cell(0, 10, f"Age: {user_data['age']}", ln=True)
        self.cell(0, 10, f"Gender: {user_data['gender']}", ln=True)
        self.cell(0, 10, f"Diet: {user_data['diet']}", ln=True)
        self.cell(0, 10, f"BMR: {user_data['bmr']} calories", ln=True)
        self.ln(5)

    def meal_section(self, meal):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, f"{meal['title']} - {meal['calories']} Calories", ln=True)

        self.set_font('Arial', 'B', 12)
        self.cell(0, 8, "Meal Items:", ln=True)
        self.set_font('Arial', '', 12)
        for item in meal['items']:
            self.multi_cell(190, 8, f"- {item}")

        self.ln(2)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 8, "Description:", ln=True)
        self.set_font('Arial', '', 12)
        self.multi_cell(190, 8, meal['description'])

        self.ln(2)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 8, "Recipe:", ln=True)
        self.set_font('Arial', '', 12)
        for step in meal['recipe'].get("steps", []):
            self.multi_cell(190, 8, f"- {step}")
        self.ln(5)

def create_meal_plan_pdf(meals_data, user_info, filename="meal_plan.pdf"):
    pdf = PDF()
    pdf.user_info(user_info)

    for meal in meals_data:
        pdf.meal_section(meal)

    pdf.output(filename)
