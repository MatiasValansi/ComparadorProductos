from abc import ABC, abstractmethod

class ProductProvider(ABC):
    """Esta clase define la interfaz que deben implementar los proveedores de productos externos."""
    @abstractmethod
    async def search(self, query: str):
        pass

    @abstractmethod
    async def get_product(self, product_id: str):
        pass
