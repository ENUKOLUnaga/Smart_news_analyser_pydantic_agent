from pydantic import BaseModel,Field

class NewsAnalysis(BaseModel):
    category: str
    summary: str
    importance_score:int = Field(..., ge=1, le=10)
