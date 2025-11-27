from typing import List

from repository.favourite_product_repository import FavoriteProductRepository
from models.favourite_product import FavouriteProduct


class FavProductService:
    """Capa de lógica de negocio para FavouriteProduct."""

    def __init__(self, repository: FavoriteProductRepository) -> None:
        self.repository = repository

    async def get_one_fav_by_id(self, favourite_id: str) -> FavouriteProduct:
        favourite = await self.repository.get_one_fav_by_id(favourite_id)
        if not favourite:
            raise Exception(f"Favourite Product not found with ID: {favourite_id}")
        return favourite

    async def get_all_favs(self) -> List[FavouriteProduct]:
        favourites = await self.repository.get_all_favs()
        if not favourites:
            raise Exception("No Favourite Products found")
        return favourites

    async def create_fav(self, fav_to_create: FavouriteProduct) -> FavouriteProduct:
        exists = await self.repository.exists(
            fav_to_create.product_url,
            fav_to_create.user_id or "",
        )
        if exists:
            raise Exception("Favourite Product already exists")
        return await self.repository.create_fav(fav_to_create)

    async def update_fav(self, favourite_id: str, fav_to_update: FavouriteProduct) -> FavouriteProduct:
        current = await self.repository.get_one_fav_by_id(favourite_id)
        if not current:
            raise Exception(f"Favourite Product not found with ID: {favourite_id}")

        if fav_to_update == current:
            raise Exception("No changes detected to update the Favourite Product")

        updated = await self.repository.update_fav(favourite_id, fav_to_update)
        if not updated:
            raise Exception(f"Favourite Product not found with ID: {favourite_id}")
        return updated

    async def delete_fav(self, favourite_id: str) -> None:
        current = await self.repository.get_one_fav_by_id(favourite_id)
        if not current:
            raise Exception(f"Favourite Product not found with ID: {favourite_id}")

        deleted = await self.repository.delete_fav(favourite_id)
        if not deleted:
            raise Exception(f"Favourite Product not found with ID: {favourite_id}")
    