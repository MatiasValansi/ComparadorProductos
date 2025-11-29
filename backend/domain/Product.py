from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
    title: str
    brand: Optional[str]
    model: Optional[str]
    price: float
    provider: str   # "mercadolibre" | "amazon"
    provider_id: str
    url: str
