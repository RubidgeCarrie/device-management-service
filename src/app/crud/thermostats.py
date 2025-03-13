from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.orm import Session, aliased

import app.models as models
import app.schemas as schemas
from app.models.devices import DeviceTypesEnum


def get_thermostat_by_id(session: Session, device_id: int) -> schemas.ThermostatDetails:
    """Fetches device details and latest status/ configuration for specified thermostat device.

    Args:
        session: Manages persistence operations for ORM-mapped objects.
        device_id: Identifier for device.

    Raises:
        HTTPException: Device not found, Invalid device ID
    """
    DeviceRegister = aliased(models.DeviceRegister)
    Thermostats = aliased(models.Thermostat)


    query = (
        session.query(DeviceRegister, Thermostats)
        .filter(DeviceRegister.id == device_id)
        .filter(DeviceRegister.device_type ==  DeviceTypesEnum.THERMOSTAT) 
        .outerjoin(
            Thermostats,
            Thermostats.device_id == DeviceRegister.id
        )
        .order_by(Thermostats.timestamp.desc())
    )
    # Get the most recent status information
    device = query.first()

    if not device:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Invalid device ID"
        )
    device_register, thermostat = device

    print("device_register", vars(device_register))
    print("thermostat",  vars(thermostat))

    # Return the device data along with the latest thermostat status
    return {
        "summary": device_register,
        "status": thermostat
    }
    # return {
    #     "summary": 
    #     {
    #         "device_id": device_register.id,
    #         "device_type": device_register.device_type,
    #         "ip_address": device_register.ip_address,
    #         "mac_address": device_register.mac_address,
    #         "registration_date": device_register.registration_date,
    #     },
    #     "status": {
    #         "status": smart_light.status,
    #         "timestamp": smart_light.timestamp,
    #     }
    # }