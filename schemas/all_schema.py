from pydantic import BaseModel
from typing import List

# Import models
from LifeSyncBackend.schemas.academics_absent_schema import AcademicsAbsentData, AcademicsAbsentDataRequest
from LifeSyncBackend.schemas.academics_assignment_schema import AcademicsAssignmentData, AcademicsAssignmentDataRequest
from LifeSyncBackend.schemas.academics_exam_schema import AcademicsExamData, AcademicsExamDataRequest
from LifeSyncBackend.schemas.academics_mark_schema import AcademicsMarkData, AcademicsMarkDataRequest
from LifeSyncBackend.schemas.activity_schema import ActivityData, ActivityDataRequest
from LifeSyncBackend.schemas.bodymeasurement_schema import BodyMeasurementData, BodyMeasurementDataRequest
from LifeSyncBackend.schemas.mind_mood_schema import MindMoodData, MindMoodDataRequest
from LifeSyncBackend.schemas.note_schema import NoteData, NoteDataRequest
from LifeSyncBackend.schemas.nutrition_schema import NutritionData, NutritionDataRequest
from LifeSyncBackend.schemas.symptom_schema import SymptomData, SymptomDataRequest
from LifeSyncBackend.schemas.time_schema import TimeData, TimeDataRequest
from LifeSyncBackend.schemas.vitals_schema import VitalsData, VitalsDataRequest
from LifeSyncBackend.schemas.workout_schema import WorkoutData, WorkoutDataRequest
from LifeSyncBackend.schemas.user_schema import UserCreate, UserLogin

from LifeSyncBackend.schemas.goals_schema import GoalsData


class AllDataRequest(BaseModel):
    version: str
    academics_absent_data: List[AcademicsAbsentData]
    academics_assignment_data: List[AcademicsAssignmentData]
    academics_mark_data: List[AcademicsMarkData]
    bodymeasurement_data: List[BodyMeasurementData]
    mind_mood_data: List[MindMoodData]
    activity_data: List[ActivityData]
    nutrition_data: List[NutritionData]
    symptom_data: List[SymptomData]
    time_data: List[TimeData]
    vitals_data: List[VitalsData]
    workout_data: List[WorkoutData]
    goals: GoalsData
