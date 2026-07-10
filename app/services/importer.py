from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.brand import Brand
from app.models.category import Category


class ImportService:

    def import_product(self, db: Session, data):

        # 1. Brand
        brand = None
        if data.get("brand"):
            brand = db.query(Brand).filter(
                Brand.name == data["brand"]
            ).first()

            if not brand:
                brand = Brand(name=data["brand"], slug=data["brand"].lower())
                db.add(brand)
                db.commit()
                db.refresh(brand)

        # 2. Category
        category = None
        if data.get("category"):
            category = db.query(Category).filter(
                Category.name == data["category"]
            ).first()

            if not category:
                category = Category(name=data["category"], slug=data["category"].lower())
                db.add(category)
                db.commit()
                db.refresh(category)

        # 3. Product
        product = Product(
            title=data["title"],
            slug=data["title"].lower().replace(" ", "-"),
            image=data.get("image"),
            brand_id=brand.id if brand else None,
            category_id=category.id if category else None,
            status="active"
        )

        db.add(product)
        db.commit()
        db.refresh(product)

        return product
