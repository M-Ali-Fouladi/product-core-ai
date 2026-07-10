from app.models.brand import Brand
from app.repositories.base import BaseRepository


class BrandRepository(BaseRepository):

    def get_by_name(self, name: str):
        return (
            self.db.query(Brand)
            .filter(Brand.name == name)
            .first()
        )

    def create(self, name: str, slug: str):
        brand = Brand(
            name=name,
            slug=slug
        )

        self.db.add(brand)
        return brand

class CategoryRepository(BaseRepository):

    def get_by_name(self, name):
        ...

    def create(self, name, slug):
        ...
class StoreRepository(BaseRepository):

    def get_by_slug(self, slug: str):
    return (
        self.db.query(Brand)
        .filter(Brand.slug == slug)
        .first()
    )

    def get_by_name(self, name):
        ...
