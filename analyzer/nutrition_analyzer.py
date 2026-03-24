from typing import List
from LifeSyncBackend.schemas.nutrition_schema import NutritionData, NutritionDataRequest

def nutrition_analyzer(data: List[NutritionData]):
    insight = [
    ]
    score = 0

    total_nutrition = len(data)

    if total_nutrition == 0:
        insight.append([
            "Nutrition",
            "No data",
            "No nutrition records found.",
            score
        ])
        return [insight, score]

    user_weight = 64 #kg
    user_height = 170 #cm
    user_age = 21
    user_gender = "M"
    user_activity = "lightly_active"

    # Calculate calories needed
    user_basal_metabolic_rate = 10 * user_weight + 6.25 * user_height - 5.0 * user_age
    if(user_gender=="F"):
        user_basal_metabolic_rate -= 161
    else:
        user_basal_metabolic_rate += 5
    '''
    If you are sedentary (little or no exercise) : Calorie-Calculation = BMR x 1.2
    If you are lightly active (light exercise/sports 1-3 days​/week) : Calorie-Calculation = BMR x 1.375
    If you are moderately active (moderate exercise/sports 3-5 days/week) : Calorie-Calculation = BMR x 1.55
    If you are very active (hard exercise/sports 6-7 days a week) : Calorie-Calculation = BMR x 1.725
    If you are extra active (very hard exercise/sports & physical job or 2x training) : Calorie-Calculation = BMR x 1.9
    '''
    total_calories_multiplier = {
        "sedentary":1.2,
        "lightly_active":1.375,
        "moderately_active":1.55,
        "very_active":1.725,
        "extra_active":1.9,
    }
    user_total_calorie_needs = user_basal_metabolic_rate * total_calories_multiplier[user_activity]

    # Add up calories, proteins, fats, carbohydrates (assuming same day)
    total_calories = 0
    total_carbs = 0
    total_fats = 0
    total_proteins = 0
    nutrition_data = data
    for item in nutrition_data:
        total_calories += item.calories
        total_carbs += item.carbs
        total_fats += item.fats
        total_proteins += item.protein

    # Energy requirements
    if(abs(total_calories-user_total_calorie_needs)<100):
        insight.append(["Nutrition", "Meeting daily energy requirements", "You are meeting your daily energy requirements of {} cal".format(int(user_total_calorie_needs))])
        score=70
    elif(total_calories<user_total_calorie_needs):
        insight.append(["Nutrition", "Consuming less than energy requirements", "You are not meeting your daily energy requirements of {} cal".format(int(user_total_calorie_needs))])
        score=50
    else:
        insight.append(["Nutrition", "Consuming more than energy requirements", "You are eating more than your daily energy requirements of {} cal".format(int(user_total_calorie_needs))])
        score=50

    # Carb requirements
    user_carbs = 130
    if(abs(total_carbs-user_carbs)<10):
        insight.append(["Nutrition", "Meeting carbohydrate requirements", "You are meeting your daily carbohydrate requirements of {} g".format(int(user_carbs))])
        score+=10
    elif(total_calories<user_carbs):
        insight.append(["Nutrition", "Short of carbohydrate requirements", "You are not meeting your daily carbohydrate requirements of {} g".format(int(user_carbs))])
    else:
        insight.append(["Nutrition", "Short of carbohydrate requirements", "You are consuming more than your daily carbohydrate requirements of {} g".format(int(user_carbs))])
        score-=10

    # Fat requirements
    user_fats_lower = user_total_calorie_needs*0.2
    user_fats_high = user_total_calorie_needs*0.35

    if(total_fats>user_fats_lower and total_fats<user_fats_high):
        insight.append(["Nutrition", "Meeting fat requirements", "You are meeting your daily fat requirements of {} g to {} g".format(int(user_fats_lower), int(user_fats_high))])
        score+=10
    elif(total_fats<user_fats_lower):
        insight.append(["Nutrition", "Short of fat requirements", "You are not meeting your fat requirements of {} g to {} g".format(int(user_fats_lower), int(user_fats_high))])
        score-=10
    else:
        insight.append(["Nutrition", "Short of fat requirements", "You are consuming more than your daily fat requirements of {} g to {} g".format(int(user_fats_lower), int(user_fats_high))])

    # Protein requirements
    protein_requirement = {
        "M":56,
        "F":46
    }
    user_proteins = protein_requirement[user_gender]
    if(abs(total_fats-user_proteins)<10):
        insight.append(["Nutrition", "Meeting protein requirements", "You are meeting your daily protein requirements of {} g".format(int(user_proteins))])
        score+=10
    elif(total_calories<user_proteins):
        insight.append(["Nutrition", "Short of protein requirements", "You are not meeting your daily protein requirements of {} g".format(int(user_proteins))])
        score-=10
    else:
        insight.append(["Nutrition", "Short of protein requirements", "You are consuming more than your daily protein requirements of {} g".format(int(user_proteins))])

    return [insight, score]
