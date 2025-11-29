from dataclasses import dataclass
from .Product import Product

@dataclass
class ProductComparisonResult:
    """Representa el resultado de comparar dos productos."""
    product_a: Product
    product_b: Product
    price_difference: float
    cheaper_provider: str
