from fastapi import FastAPI

from models.favourite_product import FavouriteProduct

from router import favourite_product_router

app = FastAPI()

app.include_router(favourite_product_router.router, prefix="/api")

#Delegar métodos HTTP a otra ruta con API-Router

@app.get("/")
def test():
    return {"message": "Testeando Backend"}

