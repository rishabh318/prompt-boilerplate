from pydantic import BaseModel
from typing import List
from app.enums.transform_type import TransformType

class TransformRequest(BaseModel):
    input_text: str
    transform_type: TransformType

class TransformResponse(BaseModel):
    outputs: List[str]
