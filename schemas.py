from pydantic import BaseModel


class DiagnosisResult(BaseModel):
    diagnosis: str
    confidence: float


class TreatmentOption(BaseModel):
    treatment: str
    success_rate: float
    duration: str


class CompleteAnalysis(BaseModel):
    result: DiagnosisResult
    options: list[TreatmentOption]