from dataclasses import dataclass


@dataclass
class ProductData:

    title: str

    brand: str | None

    category: str | None

    description: str | None

    image: str | None

    price: float | None

    currency: str | None

    external_id: str

    url: str
