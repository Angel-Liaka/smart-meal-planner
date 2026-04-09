"""
Dietary Rules for Student Nutrition Expert System
Member 1: Rule Designer
"""

# Complete rules dictionary
RULES = {
    #  DIETARY RESTRICTIONS 
    "vegan": {
        "exclude": ["meat", "poultry", "fish", "seafood", "dairy", "eggs", "honey"],
        "prioritize": ["legumes", "tofu", "tempeh", "plant_protein", "nutritional_yeast"],
        "description": "Excludes all animal-derived products"
    },
    
    "vegetarian": {
        "exclude": ["meat", "poultry", "fish", "seafood"],
        "allow": ["dairy", "eggs", "honey"],
        "description": "Excludes animal flesh but allows animal by-products"
    },
    
    "pescatarian": {
        "exclude": ["meat", "poultry"],
        "allow": ["fish", "seafood", "dairy", "eggs"],
        "description": "Vegetarian plus fish and seafood"
    },
    
    #  ALLERGIES 
    "lactose_intolerance": {
        "exclude": ["milk", "cheese", "yogurt", "cream", "butter", "whey", "casein"],
        "suggest": ["almond_milk", "soy_milk", "oat_milk", "coconut_yogurt", "lactose_free"],
        "description": "Excludes dairy products, suggests alternatives"
    },
    
    "gluten_intolerance": {
        "exclude": ["wheat", "barley", "rye", "bread", "pasta", "cereal", "beer", "flour"],
        "suggest": ["rice", "quinoa", "corn", "gluten_free_oats", "gluten_free_bread"],
        "description": "Excludes gluten-containing grains"
    },
    
    "nut_allergy": {
        "exclude": ["almonds", "walnuts", "cashews", "peanuts", "pistachios", "nut_butters"],
        "flag": ["may_contain_nuts", "processed_in_nut_facility"],
        "description": "Excludes all tree nuts and peanuts"
    },
    
    "egg_allergy": {
        "exclude": ["eggs", "mayonnaise", "albumin", "meringue"],
        "description": "Excludes eggs and egg products"
    },
    
    #  HEALTH GOALS 
    "high_protein": {
        "min_protein_per_meal": 20,
        "prioritize": [
            "chicken_breast", "turkey", "fish", "eggs", 
            "greek_yogurt", "tofu", "tempeh", "lentils", 
            "beans", "protein_powder"
        ],
        "meal_frequency": "4-6 meals per day",
        "description": "Prioritizes high-protein foods"
    },
    
    "low_carb": {
        "max_carbs_per_meal": 30,
        "exclude": ["rice", "pasta", "bread", "potatoes", "sugar", "soda", "pastries"],
        "prioritize": ["non_starchy_vegetables", "lean_protein", "healthy_fats"],
        "description": "Limits carbohydrate intake"
    },
    
    "weight_loss": {
        "calorie_deficit": 500,
        "max_calories_per_meal": 450,
        "prioritize": ["high_fiber", "high_volume", "low_calorie_density"],
        "min_water_intake": 2.5,
        "description": "Creates calorie deficit for weight loss"
    },
    
    "muscle_gain": {
        "calorie_surplus": 300,
        "min_protein_per_meal": 25,
        "meal_frequency": "5-6 meals per day",
        "prioritize": ["lean_protein", "complex_carbs", "healthy_fats"],
        "description": "Supports muscle growth with surplus calories"
    },
    
    #  ACTIVITY LEVELS 
    "activity_multipliers": {
        "sedentary": 1.2,
        "lightly_active": 1.375,
        "moderately_active": 1.55,
        "very_active": 1.725,
        "extremely_active": 1.9
    },
    
    #  MEAL DISTRIBUTION 
    "meal_distribution": {
        "breakfast": {"percentage": 0.25, "min_protein": 15},
        "lunch": {"percentage": 0.30, "min_protein": 20},
        "dinner": {"percentage": 0.30, "min_protein": 20},
        "snack": {"percentage": 0.15, "min_protein": 5}
    },
    
    #  BUDGET CONSTRAINTS 
    "budget": {
        "low": {
            "max_cost_per_meal": 350,
            "prioritize": ["beans", "lentils", "rice", "oats", "eggs", "seasonal_vegetables"],
            "description": "Budget-conscious ingredients"
        },
        "medium": {
            "max_cost_per_meal": 700,
            "allow": ["moderate_meat", "fresh_produce", "some_organic"],
            "description": "Balanced cost and quality"
        },
        "high": {
            "max_cost_per_meal": 1200,
            "allow": ["premium_ingredients", "organic", "specialty_items"],
            "description": "Premium ingredients allowed"
        }
    },
    
    #  TIME CONSTRAINTS 
    "prep_time": {
        "quick": {
            "max_minutes": 15,
            "prioritize": ["no_cook", "minimal_prep", "pre_washed", "canned_beans"],
            "description": "15 minutes or less"
        },
        "moderate": {
            "max_minutes": 30,
            "description": "30 minutes or less"
        },
        "elaborate": {
            "max_minutes": 60,
            "description": "Up to 1 hour cooking time"
        }
    }
}


def apply_rules(user_data):
    """
    Apply all rules to user inputs and return filtered recommendations
    
    Args:
        user_data (dict): User inputs including diet, allergies, goal, etc.
    
    Returns:
        dict: Applied rules with excludes, prioritizes, and constraints
    """
    excludes = []
    prioritizes = []
    constraints = {}
    
    # Apply dietary rules
    if user_data.get("diet") in RULES:
        diet_rule = RULES[user_data["diet"]]
        excludes.extend(diet_rule.get("exclude", []))
        prioritizes.extend(diet_rule.get("prioritize", []))
    
    # Apply allergy rules
    for allergy in user_data.get("allergies", []):
        allergy_key = f"{allergy}_intolerance" if allergy in ["lactose", "gluten"] else f"{allergy}_allergy"
        if allergy_key in RULES:
            allergy_rule = RULES[allergy_key]
            excludes.extend(allergy_rule.get("exclude", []))
            prioritizes.extend(allergy_rule.get("suggest", []))
    
    # Apply goal rules
    if user_data.get("goal") in RULES:
        goal_rule = RULES[user_data["goal"]]
        constraints.update(goal_rule)
        prioritizes.extend(goal_rule.get("prioritize", []))
    
    # Apply budget rules
    if user_data.get("budget") in RULES["budget"]:
        budget_rule = RULES["budget"][user_data["budget"]]
        constraints["budget"] = budget_rule
        prioritizes.extend(budget_rule.get("prioritize", []))
    
    # Apply prep time rules
    if user_data.get("prep_time") in RULES["prep_time"]:
        time_rule = RULES["prep_time"][user_data["prep_time"]]
        constraints["prep_time"] = time_rule
    
    return {
        "excludes": list(set(excludes)),
        "prioritizes": list(set(prioritizes)),
        "constraints": constraints
    }


def calculate_daily_calories(user_data):
    """Calculate daily caloric needs based on BMR and activity level"""
    weight = user_data.get("weight")
    height = user_data.get("height")
    age = user_data.get("age")
    sex = user_data.get("sex")
    activity = user_data.get("activity_level", "moderately_active")
    
    # BMR Calculation 
    if sex == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    
    # Apply activity multiplier
    multiplier = RULES["activity_multipliers"].get(activity, 1.55)
    daily_calories = bmr * multiplier
    
    # Adjust for goals
    if user_data.get("goal") == "weight_loss":
        daily_calories -= 500
    elif user_data.get("goal") == "muscle_gain":
        daily_calories += 300
    
    return {
        "bmr": round(bmr),
        "daily_calories": round(daily_calories),
        "activity_multiplier": multiplier
    }


def get_meal_calories(daily_calories, meal_type):
    """Get calorie target for specific meal"""
    distribution = RULES["meal_distribution"].get(meal_type, {"percentage": 0.25})
    return round(daily_calories * distribution["percentage"])