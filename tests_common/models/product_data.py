from dataclasses import dataclass

@dataclass
class ProductData:
    id: int
    title: str
    description: str
    price: float
    currency: str
    image: str