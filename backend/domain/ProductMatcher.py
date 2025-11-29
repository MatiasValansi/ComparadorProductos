# backend/domain/product_matcher.py
from .Product import Product

class ProductMatcher:
    @staticmethod
    def is_same_product(p1: Product, p2: Product) -> bool:
        """
        Regla simple: compara marca + modelo ignorando mayúsculas.
        Se puede expandir luego: normalización de títulos, fuzzy matching, etc.
        """
        if not p1.brand or not p2.brand:
            return False
        if not p1.model or not p2.model:
            return False

        brand_match = p1.brand.lower() == p2.brand.lower()
        model_match = p1.model.lower() == p2.model.lower()

        return brand_match and model_match
