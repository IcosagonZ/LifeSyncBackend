# Import analyzers
from LifeSyncBackend.analyzer.academics_absent_analyzer import academics_absent_analyzer
from LifeSyncBackend.analyzer.academics_assignment_analyzer import academics_assignment_analyzer
from LifeSyncBackend.analyzer.academics_exam_analyzer import academics_exam_analyzer
from LifeSyncBackend.analyzer.academics_mark_analyzer import academics_mark_analyzer
from LifeSyncBackend.analyzer.activity_analyzer import activity_analyzer
from LifeSyncBackend.analyzer.bodymeasurement_analyzer import bodymeasurement_analyzer
from LifeSyncBackend.analyzer.mind_mood_analyzer import mind_mood_analyzer
from LifeSyncBackend.analyzer.note_analyzer import note_analyzer
from LifeSyncBackend.analyzer.nutrition_analyzer import nutrition_analyzer
from LifeSyncBackend.analyzer.symptom_analyzer import symptom_analyzer
from LifeSyncBackend.analyzer.time_analyzer import time_analyzer
from LifeSyncBackend.analyzer.vitals_analyzer import vitals_analyzer
from LifeSyncBackend.analyzer.workout_analyzer import workout_analyzer

from LifeSyncBackend.schemas.all_schema import AllDataRequest

def all_analyzer(data: AllDataRequest):
    recommendation = [
    ]

    insight = [
    ]

    # Get analysis
    r1, i1 = academics_absent_analyzer(data.academics_absent_data)
    recommendation.extend(r1)
    insight.extend(i1)

    r2, i2 = academics_assignment_analyzer(data.academics_assignment_data)
    recommendation.extend(r2)
    insight.extend(i2)

    #r3, i3 = academics_exam_analyzer(data.academics_exam_data)
    #recommendation.extend(r3)
    #insight.extend(i3)

    r4, i4 = academics_mark_analyzer(data.academics_mark_data)
    recommendation.extend(r4)
    insight.extend(i4)

    r5, i5 = activity_analyzer(data.activity_data)
    recommendation.extend(r5)
    insight.extend(i5)

    r6, i6 = bodymeasurement_analyzer(data.bodymeasurement_data)
    recommendation.extend(r6)
    insight.extend(i6)

    r7, i7 = mind_mood_analyzer(data.mind_mood_data)
    recommendation.extend(r7)
    insight.extend(i7)

    #r8, i8 = note_analyzer(data.note_data)
    #recommendation.extend(r8)
    #insight.extend(i8)

    r9, i9 = nutrition_analyzer(data.nutrition_data)
    recommendation.extend(r9)
    insight.extend(i9)

    r10, i10 = symptom_analyzer(data.symptom_data)
    recommendation.extend(r10)
    insight.extend(i10)

    r11, i11 = time_analyzer(data.time_data)
    recommendation.extend(r11)
    insight.extend(i11)

    r12, i12 = vitals_analyzer(data.vitals_data)
    recommendation.extend(r12)
    insight.extend(i12)

    r13, i13 = workout_analyzer(data.workout_data)
    recommendation.extend(r13)
    insight.extend(i13)

    return [recommendation, insight]
