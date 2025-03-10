import uuid
from dataclasses import Field
from datetime import datetime
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, ConfigDict, IPvAnyAddress
from sqlalchemy.orm import Mapped, mapped_column

from app.models.devices import (DeviceTypes, SecurityCameraStatus,
                                SmartLightStatus)


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    slug: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool = False


class UserPrivate(User):
    hashed_password: str


# # --- ENUMS ---
# class DeviceTypes(str, Enum):
#     SMART_LIGHTS = "smart_lights"
#     THERMOSTATS = "thermostats"
#     SECURITY_CAMERAS = "security_cameras"

# --- BASE DEVICE SCHEMA ---
class BaseDeviceSchema(BaseModel):
    # id: uuid.UUID
    id: int
    device_id: str
    is_online: bool
    last_updated: datetime

    class Config:
        from_attributes = True  # Enables SQLAlchemy to Pydantic conversion


# --- DEVICE REGISTER RESPONSE ---
class DeviceRegisterResponse(BaseModel):
    id: int
    device_type: DeviceTypes
    # ip_address: IPvAnyAddress
    registration_date: datetime
    is_online: Optional[bool] = None
    # device_details: Optional[Union["SmartLightResponse", "ThermostatResponse", "SecurityCameraResponse"]] = None

    class Config:
        from_attributes = True


# --- SMART LIGHTS ---
class SmartLightResponse(BaseDeviceSchema):
    status: SmartLightStatus


# --- THERMOSTATS ---
class ThermostatResponse(BaseDeviceSchema):
    temperature: int
    humidity: int


# --- SECURITY CAMERAS ---
class SecurityCameraResponse(BaseDeviceSchema):
    status: SecurityCameraStatus
