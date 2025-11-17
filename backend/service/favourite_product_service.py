from repository.favourite_product_repository import FavoriteProductRepository

#Añadir validaciones y excpeciones

class FavProductService:
    def __init__(self, repository: FavoriteProductRepository):
        self.repository = repository
    
    async def get_one_fav_by_id(self, favorite_id:int):
        #Validar que esté en la BD el productoFav, sino lanzar excepción   
        return await self.repository.get_one_fav_by_id(favorite_id)

    async def get_all_favs(self):
        return await self.repository.get_all_favs()
    
    async def create_fav(self, fav_to_create):
        #Validar que no exista ya el productoFav en la BD, sino lanzar excepción
        return await self.repository.create_fav(fav_to_create)
    
    async def update_fav(self, favorite_id:int, fav_to_update):
        #Validar que esté en la BD el productoFav, sino lanzar excepción   
        return await self.repository.update_fav(favorite_id, fav_to_update)
    
    async def delete_fav(self, favorite_id:int):
        #Validar que esté en la BD el productoFav, sino lanzar excepción   
        return await self.repository.delete_fav(favorite_id)
    