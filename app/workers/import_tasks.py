from app.workers.celery_app import celery


@celery.task
def import_product_task(store: str, url: str):

    print(store)

    print(url)

    return True
