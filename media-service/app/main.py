from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Media Upload Service")

app.include_router(router, prefix="/api")
