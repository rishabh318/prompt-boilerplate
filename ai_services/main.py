from fastapi import FastAPI
from app.api.v1.transform import router as transform_router

app = FastAPI(
    title="AI Services API",
    description="Microservice for text transformation using OpenAI.",
    version="1.0.0",
    docs_url="/docs",         # Swagger UI (default)
    redoc_url="/redoc",       # ReDoc (default)
    openapi_url="/openapi.json"
)

app.include_router(
    transform_router,
    prefix="/api/v1",
    tags=["Text Transformation"]
)