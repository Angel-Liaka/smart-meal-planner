"""
Main Program - Student Nutrition Expert System
"""

from rules.dietary_rules import apply_rules, calculate_daily_calories, get_meal_calories


def get_user_input():
    """Collect user information"""
    print("\n" + "="*50)
    print("   STUDENT NUTRITION EXPERT SYSTEM")
    print("="*50)
    
    print("\n📝 Let's create your personalized meal plan!")
    
    # Personal info
    print("\n--- PERSONAL INFORMATION ---")
    age = int(input("Age: "))
    sex = input("Sex (male/female): ").lower()
    weight = float(input("Weight (kg): "))
    height = float(input("Height (cm): "))
    
    # Activity level
    print("\n--- ACTIVITY LEVEL ---")
    print("1. Sedentary (little/no exercise)")
    print("2. Lightly active (1-3 days/week)")
    print("3. Moderately active (3-5 days/week)")
    print("4. Very active (6-7 days/week)")
    print("5. Extremely active (athlete)")
    activity_choice = input("Choose (1-5): ")
    
    activity_map = {
        "1": "sedentary",
        "2": "lightly_active",
        "3": "moderately_active",
        "4": "very_active",
        "5": "extremely_active"
    }
    activity_level = activity_map.get(activity_choice, "moderately_active")
    
    # Dietary preferences
    print("\n--- DIETARY PREFERENCES ---")
    print("1. Omnivore (no restrictions)")
    print("2. Vegetarian (no meat/fish)")
    print("3. Vegan (no animal products)")
    print("4. Pescatarian (fish only)")
    diet_choice = input("Choose (1-4): ")
    
    diet_map = {
        "1": "omnivore",
        "2": "vegetarian", 
        "3": "vegan",
        "4": "pescatarian"
    }
    diet = diet_map.get(diet_choice, "omnivore")
    
    # Allergies
    print("\n--- ALLERGIES (enter multiple separated by commas) ---")
    print("Options: lactose, gluten, nuts, eggs")
    allergies_input = input("Allergies (or press Enter for none): ").lower()
    allergies = [a.strip() for a in allergies_input.split(",") if a.strip()]
    
    # Health goals
    print("\n--- HEALTH GOALS ---")
    print("1. Maintain weight")
    print("2. High protein")
    print("3. Low carb")
    print("4. Weight loss")
    print("5. Muscle gain")
    goal_choice = input("Choose (1-5): ")
    
    goal_map = {
        "1": "maintain",
        "2": "high_protein",
        "3": "low_carb",
        "4": "weight_loss",
        "5": "muscle_gain"
    }
    goal = goal_map.get(goal_choice, "maintain")
    
    # Budget
    print("\n--- BUDGET ---")
    print("1. Low (budget-friendly)")
    print("2. Medium (moderate)")
    print("3. High (premium)")
    budget_choice = input("Choose (1-3): ")
    
    budget_map = {
        "1": "low",
        "2": "medium",
        "3": "high"
    }
    budget = budget_map.get(budget_choice, "medium")
    
    # Prep time
    print("\n--- PREPARATION TIME ---")
    print("1. Quick (15 min or less)")
    print("2. Moderate (30 min or less)")
    print("3. Elaborate (up to 1 hour)")
    time_choice = input("Choose (1-3): ")
    
    time_map = {
        "1": "quick",
        "2": "moderate",
        "3": "elaborate"
    }
    prep_time = time_map.get(time_choice, "moderate")
    
    # Meal type
    print("\n--- WHAT MEAL ARE YOU PLANNING? ---")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print("4. Snack")
    meal_choice = input("Choose (1-4): ")
    
    meal_map = {
        "1": "breakfast",
        "2": "lunch",
        "3": "dinner",
        "4": "snack"
    }
    meal_type = meal_map.get(meal_choice, "lunch")
    
    return {
        "age": age,
        "sex": sex,
        "weight": weight,
        "height": height,
        "activity_level": activity_level,
        "diet": diet,
        "allergies": allergies,
        "goal": goal,
        "budget": budget,
        "prep_time": prep_time,
        "meal_type": meal_type
    }


def display_results(user_data, applied_rules, calories):
    """Display the personalized results"""
    
    print("\n" + "="*50)
    print("   YOUR PERSONALIZED MEAL PLAN")
    print("="*50)
    
    # Calorie info
    print(f"\n🔥 DAILY CALORIE TARGET: {calories['daily_calories']} kcal")
    print(f"   (Based on BMR: {calories['bmr']} kcal, Activity: {calories['activity_multiplier']}x)")
    
    # Meal calorie target
    meal_calories = get_meal_calories(calories['daily_calories'], user_data['meal_type'])
    print(f"   {user_data['meal_type'].title()} target: {meal_calories} kcal")
    
    # Restrictions
    print("\n🚫 EXCLUDED INGREDIENTS:")
    if applied_rules["excludes"]:
        for item in applied_rules["excludes"][:10]:
            print(f"   • {item}")
    else:
        print("   • No restrictions based on your inputs")
    
    # Prioritized foods
    print("\n✅ PRIORITIZED FOODS:")
    if applied_rules["prioritizes"]:
        for item in applied_rules["prioritizes"][:10]:
            print(f"   • {item}")
    else:
        print("   • No specific priorities")
    
    # Special constraints
    print("\n📋 SPECIAL CONSTRAINTS:")
    constraints = applied_rules["constraints"]
    if constraints:
        for key, value in constraints.items():
            if key not in ["prioritize", "exclude"]:
                print(f"   • {key}: {value}")
    else:
        print("   • No special constraints")
    
    print("\n" + "="*50)
    print("🎯 Based on your inputs, we can recommend meals that:")
    print(f"   • Follow {user_data['diet']} diet")
    if user_data['allergies']:
        print(f"   • Avoid {', '.join(user_data['allergies'])}")
    print(f"   • Support your {user_data['goal']} goal")
    print(f"   • Fit {user_data['budget']} budget")
    print(f"   • Take {user_data['prep_time']} prep time")
    print("="*50)


def main():
    """Main program loop"""
    print("\n WELCOME TO THE STUDENT NUTRITION EXPERT SYSTEM ")
    
    # Get user inputs
    user_data = get_user_input()
    
    # Apply rules
    applied_rules = apply_rules(user_data)
    
    # Calculate calories
    calories = calculate_daily_calories(user_data)
    
    # Display results
    display_results(user_data, applied_rules, calories)
    
    print("\n✨ Thank you for using the system! ✨")


if __name__ == "__main__":
    main()