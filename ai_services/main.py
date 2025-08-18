from fastapi import FastAPI
from app.routes.transform import router as transform_router
from app.routes.vault_routes import router as vault_router

app = FastAPI(
    title="AI Services API",
    description="Microservice for text transformation using OpenAI and Vault.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Routers (tags already set inside the router files)
# app.include_router(transform_router)
app.include_router(vault_router)

# Debug to verify routes
for route in app.routes:
    print(route.path, route.methods)
