from typing import List

from backend.domain.Product import Product
from backend.external.provider_interface import ProductProvider


class ProductSearchService:
    """Servicio de aplicación para búsqueda de productos.

    Orquesta uno o varios proveedores externos y devuelve una lista de
    productos ya normalizados al modelo de dominio `Product`.
    """

    def __init__(self, providers: List[ProductProvider]):
        # Preparado para soportar múltiples proveedores (ML, Amazon, etc.).
        self.providers = providers

    async def search_products(self, query: str) -> List[Product]:
        results: List[Product] = []
        for provider in self.providers:
            provider_results = await provider.search(query)
            results.extend(provider_results)
        return results
