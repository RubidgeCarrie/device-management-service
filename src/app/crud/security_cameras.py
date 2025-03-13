from http import HTTPStatus

import sqlalchemy
from fastapi import HTTPException
from psycopg2.errors import ForeignKeyViolation
from sqlalchemy.orm import Session, aliased

import app.models as models
import app.schemas as schemas
from app.models.devices import DeviceTypesEnum


def get_security_cameras_by_id(
    session: Session, device_id: int
) -> schemas.SecurityCameraDetails:
    """Fetches device details and latest status/ configuration for specified device.

    Args:
        session: Manages persistence operations for ORM-mapped objects.
        device_id: Identifier for device.

    Raises:
        HTTPException: Device not found, Invalid device ID
    """
    DeviceRegister = aliased(models.DeviceRegister)
    SecurityCamera = aliased(models.SecurityCamera)

    query = (
        session.query(DeviceRegister, SecurityCamera)
        .filter(DeviceRegister.id == device_id)
        .filter(DeviceRegister.device_type == DeviceTypesEnum.SECURITY_CAMERA)
        .outerjoin(SecurityCamera, SecurityCamera.device_id == DeviceRegister.id)
        .order_by(SecurityCamera.timestamp.desc())
    )
    # Get the most recent status information
    device = query.first()

    if not device:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Invalid device ID"
        )
    device_register, security_camera = device

    return {"summary": device_register, "status": security_camera}


def post_security_camera_status(
    session: Session, status: schemas.SecurityCamera
) -> schemas.SecurityCameraResponse:
    """Update

    Args:
        session: Manages persistence operations for ORM-mapped objects.
        device: Security camera status to update.

    Raises:
        HTTPException: Thermostat ID not found. Invalid thermostat device ID.
    """

    device_register = (
        session.query(models.DeviceRegister)
        .filter(models.DeviceRegister.device_type == DeviceTypesEnum.SECURITY_CAMERA)
        .filter(models.DeviceRegister.id == status.device_id)
        .first()
    )

    if not device_register:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"Device with ID {status.device_id} not found.",
        )

    updated_status = models.SecurityCamera(**status.model_dump())

    session.add(updated_status)
    session.commit()
    session.refresh(updated_status)

    return updated_status
