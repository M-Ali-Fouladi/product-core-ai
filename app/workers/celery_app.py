from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "product_ai",
    broker=f"redis://:{settings.redis_password}@{settings.redis_host}:{settings.redis_port}/0",
    backend=f"redis://:{settings.redis_password}@{settings.redis_host}:{settings.redis_port}/1",
)
