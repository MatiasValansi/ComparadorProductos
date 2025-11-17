from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, Literal
from datetime import datetime

class FavouriteProduct(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")  # Para compatibilidad con MongoDB
    title: str
    price: float
    currency: str = "ARS"
    product_url: HttpUrl
    image_url: Optional[HttpUrl]
    source: Literal["mercadolibre", "amazon", "shein"]  # origen del producto
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_checked: Optional[datetime] = None
    lowest_price_recorded: Optional[float] = None  # para comparar futuras bajas
    user_id: Optional[str] = None  # para asociar favoritos a un usuario específico
    
    def __eq__(self, other):
        if not isinstance(other, FavouriteProduct):
            return False
        return (
            self.title == other.title and
            self.price == other.price and
            self.currency == other.currency and
            self.product_url == other.product_url and
            self.source == other.source and
            self.user_id == other.user_id
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    class Config:
        allow_population_by_field_name = True  # 🔹 Permite usar 'id' o '_id'
        json_schema_extra = {
            "example": {
                "title": "Notebook HP Pavilion 15",
                "price": 699999.99,
                "currency": "ARS",
                "product_url": "https://www.mercadolibre.com.ar/p/MLA1234567",
                "image_url": "https://example.com/notebook.jpg",
                "source": "mercadolibre",
                "user_id": "user_12345"
            }
        }
