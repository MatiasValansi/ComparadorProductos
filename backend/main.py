from fastapi import FastAPI

from favourite_product import FavouriteProduct

app = FastAPI()

@app.get("/")
def test():
    return {"message": "Testeando Backend!"}

@app.get("/api/favourites/")
async def get_fav_by_id(fav_id: int):
    return {"fav_id": fav_id}

@app.get("api/favourites")
async def get_all_favs():
    return {"favourites": []}

@app.post("/api/favourites/")
async def create_fav(fav_to_create: FavouriteProduct):
    return {"fav_id": fav_to_create}

@app.put("/api/favourites/")
async def update_fav(fav_id: int, fav_to_update: FavouriteProduct):
    return {"fav_id": fav_id, "fav_updated": fav_to_update}

@app.delete("/api/favourites/")
async def delete_fav(fav_id: int):
    return {"fav_id": fav_id}

@app.delete("/api/favourites")
async def delete_all_favs():    
    return {"message": "All favourites deleted"}