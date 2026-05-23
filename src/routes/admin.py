from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/admin/generate-key")
async def create_api_key_for_auth():
    """
    In this function you should generate a api key and then
    return it back to the user
    """
    pass