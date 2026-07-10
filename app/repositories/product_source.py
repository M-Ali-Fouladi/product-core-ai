from app.models.product_source import ProductSource
from app.repositories.base import BaseRepository


class ProductSourceRepository(BaseRepository):

    def get_by_store_and_external_id(
        self,
        store_id: int,
        external_id: str,
    ):
        return (
            self.db.query(ProductSource)
            .filter(
                ProductSource.store_id == store_id,
                ProductSource.external_id == external_id,
            )
            .first()
        )

    def create(self, **kwargs):
        product_source = ProductSource(**kwargs)

        self.db.add(product_source)

        return product_source

    def update(self, product_source, **kwargs):
        for key, value in kwargs.items():
            setattr(product_source, key, value)

        return product_source
