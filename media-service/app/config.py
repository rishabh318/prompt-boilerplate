import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
    MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
    MINIO_BUCKET = os.getenv("MINIO_BUCKET")
    USE_SSL = os.getenv("USE_SSL", "false").lower() == "true"

settings = Settings()
