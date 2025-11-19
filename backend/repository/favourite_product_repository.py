from bson import ObjectId
from config.database import favourites_collection
from models.favourite_product import FavouriteProduct
from bson import ObjectId

class FavoriteProductRepository:
    
    #Realizo los métodos de la BD
    async def get_one_fav_by_id(self, favorite_id:int):
        fav_found = await favourites_collection.find_one({"_id": ObjectId(favorite_id)})
        return fav_found

    async def get_all_favs(self):
        all_favs = []
        cursor = favourites_collection.find({})
        async for document in cursor:
            all_favs.append(FavouriteProduct(document))
        return all_favs

    async def create_fav(self, fav_to_create:FavouriteProduct):
        new_fav = await favourites_collection.insert_one(fav_to_create.dict())
        fav_created = await favourites_collection.find_one({"_id": new_fav.inserted_id})
        return fav_created

    async def update_fav(self, favorite_id:int, fav_to_update:FavouriteProduct):
        await favourites_collection.update_one({"_id": favorite_id}, {"$set": fav_to_update})
        fav_updated = await favourites_collection.find_one({"_id": favorite_id})
        return fav_updated

    async def delete_fav(self, favorite_id:int):
        fav_deleted = await favourites_collection.delete_one({"_id": favorite_id})
        return fav_deleted