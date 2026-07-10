from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.product import ProductCreate, ProductOut
from app.services.product import ProductService

router = APIRouter()
service = ProductService()


@router.post("/products", response_model=ProductOut)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    return service.create_product(db, data.dict())


@router.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return service.get_product(db, product_id)


@router.get("/products")
def list_products(db: Session = Depends(get_db)):
    return service.list_products(db)
