"""
Device Registry containing summary of devices and unique identifiers.
This includes all long-lived/ immutable attributes for the device.
"""
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

import app.schemas as schemas
from app.connection import get_device_db
from app.crud.device_register import (delete_device_by_id, get_all_devices,
                                      post_device)

devices_router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
    responses={404: {"description": "Not found"}},
)

device_router = APIRouter(
    prefix="/device",
    tags=["Devices"],
    responses={404: {"description": "Not found"}},
)

# Register a New Device:
@devices_router.post(
    "/",
    status_code=HTTPStatus.OK,
    response_model=schemas.DeviceRegisterResponse,
    summary="Register a new device or replace registered device",
)
def register_device(
    device: schemas.DeviceRegister,
    session: Session = Depends(get_device_db),
):
    """API route to register a new device or replace details of an existing one"""
    return post_device(session=session, device=device)


# List All Devices:
@devices_router.get(
    "/",
    response_model=List[schemas.DeviceRegisterResponse],
    status_code=HTTPStatus.ACCEPTED,
    summary="List all registered devices",
    description="Lists all registered devices with their attributes",
)
def list_devices(
    session: Session = Depends(get_device_db),
):
    """API route to list all devices and their attributes"""
    return get_all_devices(session)


# Delete a Device:
@device_router.delete(
    "/{device_id}",
    status_code=HTTPStatus.NO_CONTENT,
    summary="Remove device from the system",
    description="Remove device and all its configuration, status data and historical records",
)
def delete_device(
    device_id: int = Path(description="Device to remove"),
    session: Session = Depends(get_device_db),
):
    """API route to delete a device and its configuration/ status data"""
    return delete_device_by_id(session, device_id)

