from fastapi import APIRouter
from app.schemas.transform import TransformRequest, TransformResponse
from app.services.transformer import transform_text

router = APIRouter()

@router.post("/transform", response_model=TransformResponse)
def transform(req: TransformRequest):
    results = transform_text(req.input_text, req.transform_type)
    return {"outputs": results}
