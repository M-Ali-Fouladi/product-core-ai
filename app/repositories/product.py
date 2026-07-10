from sqlalchemy.orm import Session
from app.models.product import Product


class ProductRepository:

    def create(self, db: Session, data):
        product = Product(**data)
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def get(self, db: Session, product_id: int):
        return db.query(Product).filter(Product.id == product_id).first()

    def list(self, db: Session, limit=20):
        return db.query(Product).limit(limit).all()
