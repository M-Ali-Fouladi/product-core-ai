from app.workers.celery_app import celery

@celery.task
def test_task(name):
    return f"Hello {name}"
