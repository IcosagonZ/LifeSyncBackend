from typing import List
from LifeSyncBackend.schemas.academics_mark_schema import AcademicsMarkData, AcademicsMarkDataRequest

def academics_mark_analyzer(data: List[AcademicsMarkData]):
    recommendation = [
    ]

    insight = [
    ]
    total_marks_obtained = 0
    total_max_marks = 0

    for item in data:
        total_marks_obtained += item.marks
        total_max_marks += item.marks_total

    if total_max_marks == 0:
        insight.append([
            "Academics",
            "No marks data",
            "No marks records available for analysis."
        ])
        return [recommendation, insight]

    percentage = (total_marks_obtained / total_max_marks) * 100

    if percentage >= 75:
        insight.append([
            "Academics",
            "Strong academic performance",
            "Your overall score is {:.2f}%. Keep up the good work!".format(percentage)
        ])

    elif percentage >= 50:
        recommendation.append([
            "Academics",
            "Average performance",
            "Your score is {:.2f}%. Try to improve your study consistency.".format(percentage)
        ])

    else:
        recommendation.append([
            "Academics",
            "Low performance",
            "Your score is {:.2f}%. Focus more on studies to improve.".format(percentage)
        ])

    insight.append([
        "Academics",
        "Total marks summary",
        "You scored {:.2f} out of {:.2f} total marks.".format(total_marks_obtained, total_max_marks)
    ])

    return [recommendation, insight]
