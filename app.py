from flask import Flask, render_template, request
import json
from rules.dietary_rules import apply_rules, calculate_daily_calories, get_meal_calories

# Flask app setup
app = Flask(__name__, static_folder='static', template_folder='templates')

# Load meals.json once at startup
with open("meals.json", "r") as f:
    meals_data = json.load(f)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/form', methods=['GET'])
def form():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    # 1️⃣ Get user inputs
    user_data = {
        "age": int(request.form.get("age")),
        "sex": request.form.get("sex"),
        "weight": float(request.form.get("weight")),
        "height": float(request.form.get("height")),
        "activity_level": request.form.get("activity_level"),
        "diet": request.form.get("diet"),
        "allergies": request.form.getlist("allergies"),
        "goal": request.form.get("goal"),
        "budget": request.form.get("budget"),
        "prep_time": request.form.get("prep_time"),
        "meal_type": request.form.get("meal_type")
    }

    # 2️⃣ Apply rules and calculate calories
    applied_rules = apply_rules(user_data)
    calories = calculate_daily_calories(user_data)
    meal_calories = get_meal_calories(calories['daily_calories'], user_data['meal_type'])

    # 3️⃣ Filter meals based on user input
    recommended_meals = []
    for meal in meals_data:
        # Must match selected meal type
        if meal["type"] != user_data["meal_type"]:
            continue
        # Must match user's diet
        if user_data["diet"] not in meal.get("diet", []):
            continue
        # Must not contain excluded ingredients
        if any(item in applied_rules["excludes"] for item in meal.get("contains", [])):
            continue
        recommended_meals.append(meal)

    # 4️⃣ Render results template
    return render_template(
        "results.html",
        user_data=user_data,
        applied_rules=applied_rules,
        calories=calories,
        meal_calories=meal_calories,
        meals=recommended_meals
    )

if __name__ == "__main__":
    app.run(debug=True)