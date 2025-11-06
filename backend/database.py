from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    DATABASE_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DATABASE_NAME]
favorites_collection = db["favorites"]

database = client.favdatabase
favorites_collection = database.favorites

#Realizo los métodos de la BD
async def get_one_fav_by_id(favorite_id):
    fav_found = await favorites_collection.find_one({"_id": favorite_id})
    return fav_found

async def get_all_favs():
    all_favs = []
    cursor = favorites_collection.find({})
    async for document in cursor:
        all_favs.append(document)
    return all_favs

async def create_fav(fav_to_create):
    result = await favorites_collection.insert_one(fav_to_create)
    return str(result.inserted_id)