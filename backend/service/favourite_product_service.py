from repository.favourite_product_repository import FavoriteProductRepository
from models.favourite_product import FavouriteProduct

#Añadir validaciones y excpeciones

class FavProductService:
    def __init__(self, repository: FavoriteProductRepository):
        self.repository = repository
    
    async def get_one_fav_by_id(self, favorite_id:int):
        #Valida que esté en la BD el productoFav, sino lanza excepción 
        prodById =  self.repository.get_one_fav_by_id(favorite_id)
        if not prodById:
            raise Exception(f"Favourite Product not found with ID: {favorite_id}")
          
        return prodById
    
    async def get_all_favs(self):        
        all_favs = self.repository.get_all_favs()
        
        if not all_favs:
            raise Exception("No Favourite Products found")
        
        return all_favs
    
    async def create_fav(self, fav_to_create:FavouriteProduct):
        #Valida que no exista ya el productoFav en la BD, sino lanza excepción
        fav_created = FavouriteProduct(fav_to_create.id, fav_to_create.title, fav_to_create.price,
                                           fav_to_create.currency, fav_to_create.product_url, fav_to_create.image_url,
                                           fav_to_create.source, fav_to_create.created_at, fav_to_create.last_checked,      fav_to_create.lowest_price_recorded,    fav_to_create.user_id   )
        
        fav_exists = await self.repository.get_one_fav_by_id(fav_created.id)
        
        if fav_exists:
            raise Exception(f"Favourite Product already exists with ID: {fav_created.id}")
        
        fav_created = self.repository.create_fav(fav_created)
        
        return await fav_created
    
    async def update_fav(self, favorite_id:int, fav_to_update):
        #Valida que esté en la BD el productoFav, sino lanza excepción
        fav_to_update_exists = await self.repository.get_one_fav_by_id(favorite_id)
        
        if not fav_to_update_exists:
            raise Exception(f"Favourite Product not found with ID: {favorite_id}")
        
        if (fav_to_update == fav_to_update_exists):
            raise Exception("No changes detected to update the Favourite Product")
        
        fav_updated = self.repository.update_fav(favorite_id, fav_to_update)
        
        return await fav_updated
    
    async def delete_fav(self, favorite_id:int):
        #Valida que esté en la BD el productoFav, sino lanza excepción
        
        fav_to_delete_exists = await self.repository.get_one_fav_by_id(favorite_id)
        
        if not fav_to_delete_exists:
            raise Exception(f"Favourite Product not found with ID: {favorite_id}")
        
        fav_deleted = self.repository.delete_fav(favorite_id)
           
        return await fav_deleted
    
    #Podría modularizar en una método la validación de existencia del fav product 
    