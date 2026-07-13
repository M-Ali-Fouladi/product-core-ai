from fastapi import APIRouter

from app.workers.import_tasks import import_product_task

router = APIRouter()


@router.post("/imports/mock")
def import_mock():

    import_product_task.delay(
        "mock",
        "https://mock.com/product/1"
    )

    return {
        "status": "queued",
        "message": "Import job has been queued."
    }
