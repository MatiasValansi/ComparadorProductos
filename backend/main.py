from fastapi import FastAPI
from dotenv import load_dotenv

from .router import favourite_product_router, product_router


# Cargar variables de entorno desde el archivo .env en el proyecto
load_dotenv()

app = FastAPI()

app.include_router(favourite_product_router.router, prefix="/api")
app.include_router(product_router.router, prefix="/api")


#Delegar métodos HTTP a otra ruta con API-Router

@app.get("/")
def test():
    return {"message": "Testeando Backend"}

