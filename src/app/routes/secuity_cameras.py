from http import HTTPStatus

from fastapi import APIRouter, Depends, Path
# from app.config import API_VERSION
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app.connection import get_device_db

security_cameras_router = APIRouter(
    prefix="/security-cameras",
    tags=["Security Cameras"],
    responses={404: {"description": "Not found"}},
)


# router = APIRouter(
#     prefix="/security_camera",
#     tags=["Security Cameras"],
#     # responses={404: {"description": "Not found"}},
# )

# Get Device Details:

# @router.put("/{device_id}", status_code=HTTPStatus.NO_CONTENT,
#             summary="Update the status or configuration of a specific device",
#             )
# def put_device_status(device_id: int = Path(description="Update security cameras configuration/status"),
#                       security_camera: SecurityCamera)
#                         session: Session = Depends(get_device_db)):
#     """API Route to update device status"""
#     return update_device_status(session, device_id, device_type)



# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results
