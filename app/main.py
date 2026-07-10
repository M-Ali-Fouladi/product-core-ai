from fastapi import FastAPI
from pydantic import BaseModel
from app.api.product import router as product_router
from app.api.import_api import router as import_router
class ProductRequest(BaseModel):
    product_id: int
    title: str

app = FastAPI()
app.include_router(product_router)
app.include_router(import_router)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "kalavofor-ai"
    }

@app.post("/product/analyze")
def analyze_product(data: ProductRequest):
    return {
        "product_id": data.product_id,
        "summary": "AI summary placeholder",
        "pros": ["good build", "fast performance"],
        "cons": ["expensive"],
        "score": 8.5
    }
