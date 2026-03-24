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
    scores = [
    ]

    insight = [
    ]

    # Get analysis
    insight_data, score_data = academics_absent_analyzer(data.academics_absent_data)
    insight.extend(insight_data)
    scores.append(score_data)

    insight_data, score_data = academics_assignment_analyzer(data.academics_assignment_data)
    insight.extend(insight_data)
    scores.append(score_data)

    #r3, i3 = academics_exam_analyzer(data.academics_exam_data)
    #scores.append(r3)
    #insight.extend(i3)

    insight_data, score_data = academics_mark_analyzer(data.academics_mark_data)
    insight.extend(insight_data)
    scores.append(score_data)

    insight_data, score_data = activity_analyzer(data.activity_data, data.goals)
    insight.extend(insight_data)
    scores.append(score_data)

    insight_data, score_data = bodymeasurement_analyzer(data.bodymeasurement_data)
    insight.extend(insight_data)
    scores.append(score_data)

    insight_data, score_data = mind_mood_analyzer(data.mind_mood_data)
    insight.extend(insight_data)
    scores.append(score_data)

    #r8, i8 = note_analyzer(data.note_data)
    #scores.append(r8)
    #insight.extend(i8)

    insight_data, score_data = nutrition_analyzer(data.nutrition_data, data.goals)
    insight.extend(insight_data)
    scores.append(score_data)

    insight_data, score_data = symptom_analyzer(data.symptom_data)
    insight.extend(insight_data)
    scores.append(score_data)

    insight_data, score_data = time_analyzer(data.time_data, data.goals)
    insight.extend(insight_data)
    scores.append(score_data)

    insight_data, score_data = vitals_analyzer(data.vitals_data)
    insight.extend(insight_data)
    scores.append(score_data)

    insight_data, score_data = workout_analyzer(data.workout_data)
    insight.extend(insight_data)
    scores.append(score_data)

    return [insight, scores]
