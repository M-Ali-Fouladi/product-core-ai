from app.repositories.product import ProductRepository


class ProductService:
    def __init__(self):
        self.repo = ProductRepository()

    def create_product(self, db, data):
        return self.repo.create(db, data)

    def get_product(self, db, product_id: int):
        return self.repo.get(db, product_id)

    def list_products(self, db, limit: int = 20):
        return self.repo.list(db, limit)
