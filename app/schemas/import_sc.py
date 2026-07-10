from pydantic import BaseModel


class ImportProduct(BaseModel):
    title: str
    brand: str | None = None
    category: str | None = None
    image: str | None = None
    external_id: str
