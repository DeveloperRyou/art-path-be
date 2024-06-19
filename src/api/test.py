from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/test",
    operation_id="test",
    summary="Test",
)
def get_result():
    return {"test": "success"}
