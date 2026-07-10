from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.import_sc import ImportProduct
from app.services.importer import ImportService

router = APIRouter()
service = ImportService()


@router.post("/import/product")
def import_product(data: ImportProduct, db: Session = Depends(get_db)):
    return service.import_product(db, data.dict())
