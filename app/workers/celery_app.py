from celery import Celery

celery = Celery(
    "product_ai",
    broker="redis://:ChooseRedisPassword@redis:6379/0",
    backend="redis://:ChooseRedisPassword@redis:6379/1",
)

celery.conf.task_track_started = True
