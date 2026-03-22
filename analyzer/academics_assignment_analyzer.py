from typing import List
from LifeSyncBackend.schemas.academics_assignment_schema import AcademicsAssignmentData
from datetime import datetime

def academics_assignment_analyzer(data: List[AcademicsAssignmentData]):
    recommendation = [
    ]

    insight = [
    ]

    pending = []
    overdue = []

    today = datetime.today().date()

    for item in data:
        if item.submitted == 0:
            due_date = datetime.strptime(item.due_date, "%Y-%m-%d").date()

            entry = "{} (Due: {})".format(item.topic, item.due_date)

            if due_date >= today:
                pending.append(entry)
            else:
                overdue.append(entry)

    if len(pending) == 0 and len(overdue) == 0:
        insight.append([
            "Academics",
            "All assignments completed",
            "You have no pending assignments."
        ])
        return [recommendation, insight]

    if len(pending) > 0:
        recommendation.append([
            "Academics",
            "Pending assignments",
            "The following assignments are to be submitted before their due dates: {}.".format(
                ", ".join(pending)
            )
        ])

    if len(overdue) > 0:
        recommendation.append([
            "Academics",
            "Overdue assignments",
            "The following assignments have passed their due dates: {}.".format(
                ", ".join(overdue)
            )
        ])

    return [recommendation, insight]