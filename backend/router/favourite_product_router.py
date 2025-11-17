from fastapi import APIRouter,HTTPException
from models.favourite_product import FavouriteProduct
from service.favourite_product_service import FavProductService
from service.favourite_product_service import FavProductService
from repository.favourite_product_repository import FavoriteProductRepository

router = APIRouter(prefix="/favourites", tags=["Favourite Products"])

service = FavProductService(FavoriteProductRepository())

@router.get("/{favourite_id}")
async def get_fav_by_id(favourite_id: int):
    try:
        fav_id = await service.get_one_fav_by_id(favourite_id)
        return fav_id
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/")
async def get_all_favs():
    try:
        all_favs = await service.get_all_favs()
        return all_favs
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", status_code=201)
async def create_fav(fav_to_create: FavouriteProduct):
    try:
        fav_created = await service.create_fav(fav_to_create)
        return fav_created
    except Exception as e:
        
        if "already exists" in str(e):
            raise HTTPException(status_code=409, detail=str(e)) 
        
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{favourite_id}")
async def update_fav(favourite_id: int, fav_to_update: FavouriteProduct):
    try:
        fav_updated = await service.update_fav(favourite_id, fav_to_update)
        return fav_updated
    except Exception as e:
        if "not found" in str(e):
            raise HTTPException(status_code=404, detail=str(e))
        elif "No changes detected" in str(e):
            raise HTTPException(status_code=400, detail=str(e))
        
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{favourite_id}")
async def delete_fav(favourite_id: int):
    try:
        fav_deleted = await service.delete_fav(favourite_id)
        return {"message": f"Favourite Product with ID {favourite_id} deleted successfully"}
    except Exception as e:
        if "not found" in str(e):
            raise HTTPException(status_code=404, detail=str(e))
        
        raise HTTPException(status_code=400, detail=str(e))
