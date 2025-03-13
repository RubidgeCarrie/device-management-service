from http import HTTPStatus

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

import app.schemas as schemas
from app.connection import get_device_db
from app.crud.security_cameras import (get_security_cameras_by_id,
                                       post_security_camera_status)

security_camera_router = APIRouter(
    prefix="/security-camera",
    tags=["Security Cameras"],
    responses={404: {"description": "Not found"}},
)

# Get Device Details:
@security_camera_router.get(
    "/{device_id}",
    response_model= schemas.SecurityCameraDetails,
    status_code= HTTPStatus.ACCEPTED,
    summary="Retrieve the latest details/status for specified security camera",
)
def get_security_cameras(
    device_id: int = Path(
        description="Filter to only return status/configuration information for given security camera"
    ),
    session: Session = Depends(get_device_db),
):
    """API route to fetch a device by ID."""
    return get_security_cameras_by_id(session=session, device_id=device_id)

# Update Device Status:
@security_camera_router.post(
    "/{device_id}",
    status_code=HTTPStatus.OK,
    response_model=schemas.SecurityCameraResponse,
    summary="Update security camera device status",
)
def update_status(
    status: schemas.SecurityCamera,
    session: Session = Depends(get_device_db),
):
    """API route to to update a thermostat status"""
    return post_security_camera_status(session=session, status=status)