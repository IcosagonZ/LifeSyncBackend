from typing import List
from LifeSyncBackend.schemas.academics_absent_schema import AcademicsAbsentData, AcademicsAbsentDataRequest

def academics_absent_analyzer(data: List[AcademicsAbsentData]):
    recommendation = [
    ]

    insight = [
    ]

    total_absences = len(data)

    if total_absences == 0:
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

    return [recommendation, insight]
