from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
from favourite_product import FavouriteProduct

class Settings(BaseSettings):
    MONGO_URI: str
    DATABASE_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DATABASE_NAME]
favourites_collection = db["favorites"]

database = client.favdatabase
favourites_collection = database.favorites

