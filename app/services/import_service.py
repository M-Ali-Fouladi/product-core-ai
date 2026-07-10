from sqlalchemy.orm import Session


class ImportService:

    def __init__(self, db: Session):
        self.db = db

    def import_product(self, product_data):
    pass
