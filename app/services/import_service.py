from sqlalchemy.orm import Session
from app.repositories.brand import BrandRepository
from app.repositories.category import CategoryRepository
from app.repositories.product import ProductRepository
from app.repositories.product_source import ProductSourceRepository
from app.repositories.store import StoreRepository
from slugify import slugify

class ImportService:

    def __init__(self, db: Session):

        self.db = db
        self.brand_repo = BrandRepository(db)
        self.category_repo = CategoryRepository(db)
        self.product_repo = ProductRepository(db)
       	self.product_source_repo = ProductSourceRepository(db)
	self.store_repo = StoreRepository(db)	
    
    def import_product(self, product_data):

    try:

        brand = self._get_or_create_brand(product_data)

        category = self._get_or_create_category(product_data)

        store = self._get_store(product_data)

        product = self._create_product(
            product_data,
            brand,
            category,
        )

        self._create_product_source(
            product,
            store,
            product_data,
        )

        self.db.commit()

        return product

    except Exception:

        self.db.rollback()

        raise

    def _get_or_create_brand(self, product_data):

    if not product_data.brand:
        return None

    #brand = self.brand_repo.get_by_name(product_data.brand)
    slug = slugify(product_data.brand)
    brand = self.brand_repo.get_by_slug(slug)
   
    if brand:
        return brand

    brand = self.brand_repo.create(
        name=product_data.brand,
        slug=slugify(product_data.brand)
    )

    return brand

    def _get_or_create_category(self, product_data):

    if not product_data.category:
        return None

    #category = self.category_repo.get_by_name(product_data.category)
    slug = slugify(product_data.category)
    category = self.category_repo.get_by_slug(slug)
    if category:
        return category

    category = self.category_repo.create(
        name=product_data.category,
        slug=slugify(product_data.category)
    )

    return category

    def _get_store(self, product_data):
      store = self.store_repo.get_by_slug(product_data.store)
      if not store:
            raise ValueError(f"Store '{product_data.store}' not found.")
      return store

    def get_by_slug(self, slug: str):
      return (self.db.query(Store).filter(Store.slug == slug).first())

    def _create_product(self,product_data,brand,category):

    product = self.product_repo.create(
        title=product_data.title,
        slug=slugify(product_data.title),
        brand_id=brand.id if brand else None,
        category_id=category.id if category else None,
        image=product_data.image)
    self.db.flush()

    return product
    def _create_product_source(self,product,store,product_data):

    source = self.product_source_repo.get_by_store_and_external_id(
        store.id,
        product_data.external_id)

    if source:
        self.product_source_repo.update(
            source,
            last_price=product_data.price,
            currency=product_data.currency,
            url=product_data.url,
        )
        return source

    return self.product_source_repo.create(
        product_id=product.id,
        store_id=store.id,
        external_id=product_data.external_id,
        url=product_data.url,
        currency=product_data.currency,
        last_price=product_data.price,
    )
