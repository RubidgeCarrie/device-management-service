from importlib import import_module

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import text
from api.config import API_VERSION
from sqlalchemy.ext.asyncio import AsyncSession
from api.models.devices import DEVICE_TYPE_MODEL_MAP, DeviceRegister

from device_db.connection import get_device_db


api = import_module(f".{API_VERSION}", package="app.api")
router = APIRouter()


@router.get(
    "/device/{device_id}",
    response_model=dict,
    tags=["Device"],
)
async def get_device_details(device_id: int, session: AsyncSession = Depends(get_async_session)):
    # Fetch the main device entry
    result = await session.execute(select(DeviceRegister).where(DeviceRegister.id == device_id))
    device = result.scalars().first()

    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    # Dynamically get the correct related table
    related_model = DEVICE_TYPE_MODEL_MAP.get(device.device_type.value)

    # Fetch related data using JOIN if model exists
    related_data = None
    if related_model:
        join_result = await session.execute(
            select(DeviceRegister, related_model)
            .join(related_model, related_model.device_id == DeviceRegister.id, isouter=True)
            .where(DeviceRegister.id == device_id)
            .options(joinedload(DeviceRegister))
        )
        related_data = join_result.first()[1] if join_result.first() else None

    return {
        "id": device.id,
        "device_type": device.device_type.value,
        "ip_address": str(device.ip_address),
        "registration_date": device.registration_date,
        "is_online": related_data.is_online if related_data else None,
        "device_details": related_data
    }