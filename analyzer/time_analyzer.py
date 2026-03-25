from typing import List
from LifeSyncBackend.schemas.time_schema import TimeData, TimeDataRequest
from LifeSyncBackend.schemas.goals_schema import GoalsData

def time_analyzer(data: List[TimeData], goals: GoalsData):
    insight = [
    ]
    score = 0

    time_goals = {
        "study": goals.study*60,
        "sleep": goals.sleep*60,
        "exercise": goals.exercise*60,
    }

    event_time = {}

    for item in data:
        event = item.event.lower()

        if event in event_time:
            event_time[event] += item.duration
        else:
            event_time[event] = item.duration

    if len(event_time) == 0:
        insight.append([
            "Time",
            "No data",
            "No time records found."
        ])
        return [insight, score]

    for event in time_goals:
        goal = time_goals[event]
        actual = event_time.get(event, 0)

        if actual >= goal:
            score += 25
            insight.append([
                "Time",
                "{} goal met".format(event.capitalize()),
                "You spent {} minutes on {} and met your goal of {} minutes.".format(actual, event, goal)
            ])

        elif actual >= goal - 10:
            score += 20
            insight.append([
                "Time",
                "{} nearly met".format(event.capitalize()),
                "You spent {} minutes on {}. You are close to the goal of {} minutes.".format(actual, event, goal)
            ])

        else:
            insight.append([
                "Time",
                "{} below goal".format(event.capitalize()),
                "You spent {} minutes on {}. Try to reach {} minutes.".format(actual, event, goal)
            ])

    if(score>100):
        score=100

    return [insight, score]
