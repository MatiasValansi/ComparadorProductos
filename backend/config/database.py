from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    DATABASE_NAME: str
    CLUSTER_PASS: str

    class Config:
        env_file = "backend/.env"

settings = Settings()

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DATABASE_NAME]
favourites_collection = db["favorites"]


