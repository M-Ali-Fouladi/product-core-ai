from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.importers.factory import ImportFactory
from app.services.import_service import ImportService

router = APIRouter()


@router.post("/imports/mock")
def import_mock(db: Session = Depends(get_db)):

    importer = ImportFactory.get_importer("mock")

    product_data = importer.import_product(
        "https://mock.com/product/1"
    )

    service = ImportService(db)

    product = service.import_product(product_data)

    return {
        "id": product.id,
        "title": product.title,
    }
