import datetime
from http import HTTPStatus
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas


def get_all_devices(session: Session) -> List[schemas.DeviceRegisterResponse]:
    """Fetches all devices and their attributes from the device registry.

    Args:
        session: Manages persistence operations for ORM-mapped objects.
    """  
    devices = session.query(models.DeviceRegister).all()

    return [schemas.DeviceRegisterResponse.model_validate(device) for device in devices]


def delete_device_by_id(session: Session, device_id: int) -> None:
    """Deletes a device from the device register.

    The delete cascasde on the device_id will remove its status and historic data.

    Args:
        session: Manages persistence operations for ORM-mapped objects.
        device_id: Identifier for device.

    Raises:
        HTTPException: Device not found, Invalid device ID.
    """
    device = (
        session.query(models.DeviceRegister)
        .filter(models.DeviceRegister.id == device_id)
        .first()
    )

    if not device:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Invalid device ID"
        )

    session.delete(device)
    session.commit()

    return {"message": "Device deleted successfully"}


def post_device(session: Session, device: schemas.DeviceRegister) -> schemas.DeviceRegisterResponse:
    """Register a new IoT device.

    Args:
        session: Manages persistence operations for ORM-mapped objects.
        device: Device to register.
    """
    # Convert ip_address to string
    device_dict = device.model_dump()
    device_dict["ip_address"] = str(device_dict["ip_address"])

    new_device = models.DeviceRegister(**device_dict) 

    session.add(new_device)
    session.commit()
    session.refresh(new_device)

    return new_device

