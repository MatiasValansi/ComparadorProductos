from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    """Modelo de dominio para un producto comparado entre proveedores externos.

    No expone detalles específicos del proveedor más allá de:
    - `provider`: nombre del proveedor (ej. "mercadolibre", "amazon").
    - `provider_id`: identificador interno del proveedor.
    - `url`: enlace canónico al detalle del producto (permalink).
    - `image_url`: URL de una imagen representativa.
    """

    title: str
    brand: Optional[str]
    model: Optional[str]
    price: float
    provider: str   # "mercadolibre" | "amazon" | etc.
    provider_id: str
    url: str
    image_url: Optional[str] = None
