from typing import List

from fastapi import APIRouter, HTTPException

from backend.models.favourite_product import FavouriteProduct
from backend.repository.favourite_product_repository import FavoriteProductRepository
from backend.service.favourite_product_service import FavProductService


router = APIRouter(prefix="/favourites", tags=["Favourite Products"])

service = FavProductService(FavoriteProductRepository())


@router.get("/{favourite_id}", response_model=FavouriteProduct)
async def get_fav_by_id(favourite_id: str):
    try:
        return await service.get_one_fav_by_id(favourite_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.get("/", response_model=List[FavouriteProduct])
async def get_all_favs():
    try:
        return await service.get_all_favs()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", status_code=201, response_model=FavouriteProduct)
async def create_fav(fav_to_create: FavouriteProduct):
    try:
        return await service.create_fav(fav_to_create)
    except Exception as e:
        message = str(e)
        if "already exists" in message:
            raise HTTPException(status_code=409, detail=message)
        raise HTTPException(status_code=400, detail=message)
    

@router.put("/{favourite_id}", response_model=FavouriteProduct)
async def update_fav(favourite_id: str, fav_to_update: FavouriteProduct):
    try:
        return await service.update_fav(favourite_id, fav_to_update)
    except Exception as e:
        message = str(e)
        if "not found" in message:
            raise HTTPException(status_code=404, detail=message)
        if "No changes detected" in message:
            raise HTTPException(status_code=400, detail=message)
        raise HTTPException(status_code=400, detail=message)
    

@router.delete("/{favourite_id}")
async def delete_fav(favourite_id: str):
    try:
        await service.delete_fav(favourite_id)
        return {"message": f"Favourite Product {favourite_id} deleted successfully"}
    except Exception as e:
        message = str(e)
        if "not found" in message:
            raise HTTPException(status_code=404, detail=message)
        raise HTTPException(status_code=400, detail=message)


class Config:
    env_file = "backend/.env"