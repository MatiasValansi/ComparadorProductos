from abc import ABC, abstractmethod
from typing import List

from backend.domain.Product import Product


class ProductProvider(ABC):
    """Interfaz que deben implementar los proveedores externos de productos.

    Cada proveedor (Mercado Libre, Amazon, etc.) debe exponer al menos
    un método de búsqueda unificada sobre el modelo de dominio `Product`.
    """

    @abstractmethod
    async def search(self, query: str) -> List[Product]:
        """Busca productos por `query` y devuelve una lista de `Product` normalizados."""

    @abstractmethod
    async def get_product(self, product_id: str) -> Product:
        """Obtiene el detalle de un producto individual del proveedor externo."""
