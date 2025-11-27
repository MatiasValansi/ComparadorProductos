from bson import ObjectId
from pydantic import HttpUrl

from config.database import favourites_collection
from models.favourite_product import FavouriteProduct


class FavoriteProductRepository:
    """Capa de acceso a datos para FavouriteProduct.

    - Solo habla con Mongo (motor).
    - Devuelve y recibe modelos de dominio (`FavouriteProduct`).
    - Se encarga de convertir `ObjectId` <-> `str` y URLs.
    """

    async def get_one_fav_by_id(self, favourite_id: str) -> FavouriteProduct | None:
        try:
            document = await favourites_collection.find_one({"_id": ObjectId(favourite_id)})
            return FavouriteProduct(**self._deserialize_document(document)) if document else None
        except Exception:
            return None

    async def get_all_favs(self) -> list[FavouriteProduct]:
        favourites: list[FavouriteProduct] = []
        cursor = favourites_collection.find({})
        async for document in cursor:
            favourites.append(FavouriteProduct(**self._deserialize_document(document)))
        return favourites

    async def create_fav(self, fav: FavouriteProduct) -> FavouriteProduct:
        document = self._serialize_fav(fav)

        # Dejamos que Mongo genere el ObjectId
        document.pop("_id", None)

        result = await favourites_collection.insert_one(document)
        created = await favourites_collection.find_one({"_id": result.inserted_id})
        return FavouriteProduct(**self._deserialize_document(created))

    async def update_fav(self, favourite_id: str, fav_to_update: FavouriteProduct) -> FavouriteProduct | None:
        oid = ObjectId(favourite_id)
        await favourites_collection.update_one(
            {"_id": oid},
            {"$set": self._serialize_fav(fav_to_update)},
        )
        updated = await favourites_collection.find_one({"_id": oid})
        return FavouriteProduct(**self._deserialize_document(updated)) if updated else None

    async def delete_fav(self, favourite_id: str) -> bool:
        oid = ObjectId(favourite_id)
        result = await favourites_collection.delete_one({"_id": oid})
        return result.deleted_count == 1

    async def exists(self, product_url: HttpUrl, user_id: str) -> bool:
        document = await favourites_collection.find_one(
            {
                "product_url": str(product_url),
                "user_id": user_id,
            }
        )
        return document is not None

    def _serialize_fav(self, fav: FavouriteProduct) -> dict:
        """Convierte un FavouriteProduct a dict listo para MongoDB."""

        data = fav.model_dump(by_alias=True)

        data["product_url"] = str(data["product_url"])
        if data.get("image_url") is not None:
            data["image_url"] = str(data["image_url"])

        # Si el id viene como string, convertirlo a ObjectId
        if data.get("_id"):
            try:
                data["_id"] = ObjectId(data["_id"])
            except Exception:
                data.pop("_id", None)

        return data

    def _deserialize_document(self, document: dict) -> dict:
        """Normaliza un documento de MongoDB para el modelo Pydantic."""

        if not document:
            return {}

        doc = document.copy()
        if isinstance(doc.get("_id"), ObjectId):
            doc["_id"] = str(doc["_id"])
        return doc
