from pydantic import BaseModel


class ProductCreate(BaseModel):
    title: str
    slug: str
    brand_id: int | None = None
    category_id: int | None = None
    image: str | None = None


class ProductOut(BaseModel):
    id: int
    title: str
    slug: str

    class Config:
        from_attributes = True
