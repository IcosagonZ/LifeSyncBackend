from typing import List
from LifeSyncBackend.schemas.academics_mark_schema import AcademicsMarkData, AcademicsMarkDataRequest

def academics_mark_analyzer(data: List[AcademicsMarkData]):
    insight = [
    ]
    score = 0

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
        return [insight, score]

    percentage = (total_marks_obtained / total_max_marks) * 100

    if percentage >= 75:
        score = 100
        insight.append([
            "Academics",
            "Strong academic performance",
            "Your overall score is {:.2f}%. Keep up the good work!".format(percentage)
        ])

    elif percentage >= 50:
        score = 50
        recommendation.append([
            "Academics",
            "Average performance",
            "Your score is {:.2f}%. Try to improve your study consistency.".format(percentage)
        ])

    else:
        score = 20
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

    return [insight, score]
