from typing import List
from LifeSyncBackend.schemas.academics_absent_schema import AcademicsAbsentData, AcademicsAbsentDataRequest

def academics_absent_analyzer(data: List[AcademicsAbsentData]):
    insight = [
    ]
    score = 0

    total_absences = len(data)

    if total_absences == 0:
        score = 100
        insight.append([
            "Academics",
            "Perfect attendance",
            "You were present every day."
        ])
    else:
        insight.append([
            "Academics",
            "Absence record",
            "You were absent for {} days.".format(total_absences)
        ])
        score = 100 - (total_absences*5)
        if(score<0):
            score = 0

    return [insight, score]
