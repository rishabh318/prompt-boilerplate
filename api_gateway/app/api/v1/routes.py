from fastapi import APIRouter, Request
import httpx

router = APIRouter()

AI_SERVICE_URL = "http://ai_services:8000"  # Docker Compose DNS

@router.post("/ai/transform")
async def proxy_ai_transform(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AI_SERVICE_URL}/transform", json=body)
    return response.json()
