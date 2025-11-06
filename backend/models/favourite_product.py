from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, Literal
from datetime import datetime

class FavouriteProduct(BaseModel):
    id: Optional[str] = Field(alias="_id")  # Para compatibilidad con MongoDB
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

    class Config:
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
