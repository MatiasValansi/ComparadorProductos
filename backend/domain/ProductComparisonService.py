from .Product import Product
from .ProductComparisonResult import ProductComparisonResult

class ProductComparisonService:
    """Servicio de dominio puro que calcula diferencias de precio y determina el más barato."""
    def compare(self, p1: Product, p2: Product) -> ProductComparisonResult:
        price_diff = abs(p1.price - p2.price)
        cheaper = p1.provider if p1.price < p2.price else p2.provider

        return ProductComparisonResult(
            product_a=p1,
            product_b=p2,
            price_difference=price_diff,
            cheaper_provider=cheaper
        )
