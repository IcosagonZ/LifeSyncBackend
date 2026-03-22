from typing import List
from LifeSyncBackend.schemas.vitals_schema import VitalsData, VitalsDataRequest

def vitals_analyzer(data: List[VitalsData]):
    recommendation = [
    ]

    insight = [
    ]

    if len(data) == 0:
        insight.append([
            "Vitals",
            "No data",
            "No vital records found."
        ])
        return [recommendation, insight]

    for item in data:
        insight.append([
            "Vitals",
            "{} recorded".format(item.type.capitalize()),
            "Your {} is {} {}".format(item.type, item.value, item.unit)
        ])

    return [recommendation, insight]