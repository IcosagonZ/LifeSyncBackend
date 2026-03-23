from typing import List
from LifeSyncBackend.schemas.bodymeasurement_schema import BodyMeasurementData, BodyMeasurementDataRequest

def bodymeasurement_analyzer(data: List[BodyMeasurementData]):
    recommendation = [
    ]

    insight = [
    ]
   
    user_weight = None
    user_height = None
    weight_unit = "kg"
    height_unit = "cm"

    for item in data:
        if item.measurement_type.lower() == "weight":
            user_weight = item.value
            weight_unit = item.unit.lower()

        elif item.measurement_type.lower() == "height":
            user_height = item.value
            height_unit = item.unit.lower()

    if user_weight is None or user_height is None:
        insight.append([
            "Body",
            "Insufficient data",
            "Height or weight data missing for BMI calculation."
        ])

    if weight_unit == "kg":
        weight_kg = user_weight
    elif weight_unit == "lb":
        weight_kg = user_weight * 0.453592
    else:
        weight_kg = user_weight  

    if height_unit == "cm":
        height_m = user_height / 100
    elif height_unit == "m":
        height_m = user_height
    elif height_unit == "inch":
        height_m = user_height * 0.0254
    else:
        height_m = user_height / 100  

    user_bmi = weight_kg / (height_m * height_m)

    bmi_ranges = {
        "underweight": 18.5,
        "normal": 24.9,
        "overweight": 29.9
    }

    if user_bmi < bmi_ranges["underweight"]:
        recommendation.append([
            "Body",
            "Underweight",
            "Your BMI is {:.2f}. You are below the healthy range.".format(user_bmi)
        ])

    elif user_bmi <= bmi_ranges["normal"]:
        insight.append([
            "Body",
            "Healthy BMI",
            "Your BMI is {:.2f}. You are within the normal range.".format(user_bmi)
        ])

    elif user_bmi <= bmi_ranges["overweight"]:
        recommendation.append([
            "Body",
            "Overweight",
            "Your BMI is {:.2f}. Consider regular exercise and balanced diet.".format(user_bmi)
        ])

    else:
        recommendation.append([
            "Body",
            "Obese",
            "Your BMI is {:.2f}. It is advisable to adopt a healthier lifestyle.".format(user_bmi)
        ])

    insight.append([
        "Body",
        "BMI value",
        "Your calculated BMI is {:.2f}.".format(user_bmi)
    ])

    return [recommendation, insight]
