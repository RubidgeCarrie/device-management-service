# from importlib import import_module

from http import HTTPStatus

from fastapi import APIRouter, Depends, Path
# from app.config import API_VERSION
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app.connection import get_device_db
from app.crud.devices import (delete_device_by_id, get_device_by_id,
                              get_user_by_id)
from app.schemas.devices import DeviceRegisterResponse, User

# from requests import HTTPStatus


# API_VERSION = "v1"
# api = import_module(f".{API_VERSION}", package="app.api")
router = APIRouter()

router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{device_id}", response_model=DeviceRegisterResponse, status_code=HTTPStatus.ACCEPTED, 
            summary="List all registered devices", description="Lists all registered devices with their configuration",
            )
def get_user(device_id: int = Path(description="Filter to only return configuration for specific device"), session: Session = Depends(get_device_db)):
    """API route to fetch a device by ID)."""
    return get_device_by_id(session, device_id)


@router.delete("/{device_id}", status_code=HTTPStatus.NO_CONTENT,
               summary="Remove device from the system" , description="Remove device and all its configuration, status data and historical records")
def delete_device(device_id:int = Path(description="Device to remove"), session: Session = Depends(get_device_db)):
    """API route to delete a device and its configuration/ status data"""
    return delete_device_by_id(session, device_id)


@router.put("/{device_id}", status_code=HTTPStatus.NO_CONTENT,
            summary="Update the status or configuration of a specific device",
            )
def put_device_status(device_id: int = Path(description="Device to update"),  session: Session = Depends(get_device_db)):
    """API Route to update device status"""
    return update_device_status(session, device_id, device_type)

# DEVICE_TYPE_MODEL_MAP = {
#     DeviceTypes.SMART_LIGHTS: (SmartLights, SmartLightResponse),
#     DeviceTypes.THERMOSTATS: (Thermostats, ThermostatResponse),
#     DeviceTypes.SECURITY_CAMERAS: (SecurityCameras, SecurityCameraResponse),
# }

# @router.get(
#     "/device/{device_id}",
#     response_model=DeviceRegisterResponse,
#     tags=["Device"],
# )
# async def get_device_details(device_id: UUID, session: AsyncSession = Depends(get_device_db)):
#     """Fetches device details including type-specific data."""

#     # Fetch the main device entry
#     result = await session.execute(select(DeviceRegister).where(DeviceRegister.id == device_id))
#     device = result.scalars().first()

#     if not device:
#         raise HTTPException(status_code=404, detail="Device not found")
    
#     # Get the appropriate related model & response schema
#     related_model, response_schema = DEVICE_TYPE_MODEL_MAP.get(device.device_type, (None, None))

#     related_data = None
#     if related_model:
#         join_result = await session.execute(
#             select(related_model)
#             .where(related_model.device_id == device.id)
#             .options(joinedload(related_model))
#         )
#         db_related_data = join_result.scalars().first()

#         # Convert SQLAlchemy ORM object to Pydantic schema
#         if db_related_data:
#             related_data = response_schema.model_validate(db_related_data)

#     return DeviceRegisterResponse(
#         id=device.id,
#         device_type=device.device_type,
#         ip_address=device.ip_address,
#         registration_date=device.registration_date,
#         is_online=related_data.is_online if related_data else None,
#         device_details=related_data,
#     )

# @router.get(
#     "/device/{device_id}",
#     response_model=DeviceRegisterResponse,
#     tags=["Device"],
# )
# async def get_device_details(device_id: UUID, session: AsyncSession = Depends(get_device_db)):
#     """Fetches device details including type-specific data."""

#     # Fetch the main device entry
#     result = await session.execute(select(DeviceRegister).where(DeviceRegister.id == device_id))
#     device = result.scalars().first()

#     if not device:
#         raise HTTPException(status_code=404, detail="Device not found")

#     return device
    