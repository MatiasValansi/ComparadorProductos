from typing import List
from backend.domain.Product import Product
from backend.external.provider_interface import ProductProvider

class ProductSearchService:

    def __init__(self, provider: ProductProvider):
        self.provider = provider

    async def search_products(self, query: str) -> List[Product]:
        return await self.provider.search(query)
