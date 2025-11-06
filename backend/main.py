from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
    return {"message": "Testeando Backend!"}

@app.get("/api/favourites/{fav_id}")
async def get_fav_by_id(fav_id: int):
    return {"fav_id": fav_id}

@app.get("api/favourites")
async def get_all_favs():
    return {"favourites": []}

@app.post("/api/favourites/{fav_id}")
async def create_fav(fav_id: int):
    return {"fav_id": fav_id}

@app.put("/api/favourites/{fav_id}")
async def update_fav(fav_id: int):
    return {"fav_id": fav_id}

@app.delete("/api/favourites/{fav_id}")
async def delete_fav(fav_id: int):
    return {"fav_id": fav_id}

@app.delete("/api/favourites")
async def delete_all_favs():    
    return {"message": "All favourites deleted"}