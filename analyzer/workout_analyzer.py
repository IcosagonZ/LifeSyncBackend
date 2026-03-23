from typing import List
from LifeSyncBackend.schemas.workout_schema import WorkoutData, WorkoutDataRequest

def workout_analyzer(data: List[WorkoutData]):
    recommendation = [
    ]

    insight = [
    ]

    total_workouts = len(data)

    if total_workouts == 0:
        insight.append([
            "Workout",
            "No data",
            "No workout records found."
        ])
        return [recommendation, insight]

    insight.append([
        "Workout",
        "Workout summary",
        "You performed {} workouts.".format(total_workouts)
    ])

    for item in data:
        insight.append([
            "Workout",
            "{} session".format(item.name),
            "Duration: {} mins, Calories: {}".format(item.duration, item.calories)
        ])

    return [recommendation, insight]
