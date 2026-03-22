from typing import List
from LifeSyncBackend.schemas.activity_schema import ActivityData, ActivityDataRequest

def activity_analyzer(data: List[ActivityData]):
    recommendation = [
    ]

    insight = [
    ]

    total_duration = 0
    total_calories = 0
    total_distance = 0

    for item in data:
        total_duration += item.duration
        total_calories += item.calories
        total_distance += item.distance

    total_sessions = len(data)

    if total_sessions == 0:
        insight.append([
            "Activity",
            "No activity data",
            "No physical activity records found."
        ])
        return [recommendation, insight]

    avg_duration = total_duration / total_sessions

    if avg_duration >= 30:
        insight.append([
            "Activity",
            "Good activity level",
            "You are active with an average of {:.2f} minutes per session.".format(avg_duration)
        ])

    elif avg_duration >= 15:
        recommendation.append([
            "Activity",
            "Moderate activity",
            "Your activity level is {:.2f} minutes. Try to increase daily exercise.".format(avg_duration)
        ])

    else:
        recommendation.append([
            "Activity",
            "Low activity level",
            "You are only active for {:.2f} minutes. Increase physical activity for better health.".format(avg_duration)
        ])

    insight.append([
        "Activity",
        "Calories burned",
        "You burned a total of {:.2f} calories.".format(total_calories)
    ])

    insight.append([
        "Activity",
        "Distance covered",
        "You covered a total distance of {} units.".format(total_distance)
    ])

    return [recommendation, insight]
