from typing import List
from LifeSyncBackend.schemas.activity_schema import ActivityData, ActivityDataRequest
from LifeSyncBackend.schemas.goals_schema import GoalsData

def activity_analyzer(data: List[ActivityData], goals: GoalsData):
    insight = [
    ]
    score = 0

    step_goal = goals.steps
    distance_goal = goals.distance

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
        return [insight, score]

    avg_duration = total_duration / total_sessions

    if avg_duration >= 30:
        score = 50
        insight.append([
            "Activity",
            "Good activity level",
            "You are active with an average of {:.2f} minutes per session.".format(avg_duration)
        ])

    elif avg_duration >= 15:
        score = 40
        recommendation.append([
            "Activity",
            "Moderate activity",
            "Your activity level is {:.2f} minutes. Try to increase daily exercise.".format(avg_duration)
        ])

    else:
        score = 0
        recommendation.append([
            "Activity",
            "Low activity level",
            "You are only active for {:.2f} minutes. Increase physical activity for better health.".format(avg_duration)
        ])

    if total_distance >= distance_goal:
        score += 25
        insight.append([
            "Activity",
            "Distance goal met",
            "You covered {:.2f} units and met your distance goal of {} units.".format(total_distance, distance_goal)
        ])
    else:
        recommendation.append([
            "Activity",
            "Distance below goal",
            "You covered {:.2f} units. Try to reach {} units.".format(total_distance, distance_goal)
        ])

    steps_estimated = total_distance * 1300

    if steps_estimated >= step_goal:
        score += 25
        insight.append([
            "Activity",
            "Step goal met",
            "You achieved approximately {} steps, meeting your goal of {} steps.".format(int(steps_estimated), step_goal)
        ])
    else:
        recommendation.append([
            "Activity",
            "Step goal not met",
            "You achieved approximately {} steps. Try to reach {} steps.".format(int(steps_estimated), step_goal)
        ])

    insight.append([
        "Activity",
        "Calories burned",
        "You burned a total of {:.2f} calories.".format(total_calories)
    ])

    insight.append([
        "Activity",
        "Distance covered",
        "You covered a total distance of {:.2f} units.".format(total_distance)
    ])

    return [insight, score]
