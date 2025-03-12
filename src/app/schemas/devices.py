import uuid
from dataclasses import Field
from datetime import datetime
from enum import Enum
from typing import Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, IPvAnyAddress, constr
from sqlalchemy.orm import Mapped, mapped_column

from app.models.devices import (DeviceTypes, SecurityCameraStatus,
                                SmartLightStatus)


class DeviceRegister(BaseModel):

    device_type: DeviceTypes
    ip_address: IPvAnyAddress
    mac_address: Optional[str] = None
    registration_date: datetime

    class Config:
        orm_mode = True
        from_attributes = True
        use_enum_values = True
        json_schema_extra= {
            "examples": [
{
                        "device_type": "smart_light",
                        "ip_address": "192.168.1.10",
                        "mac_address": "00:1a:2b:3c:4d:5e",
                        "registration_date": "2025-03-12T17:51:02.426Z",
            }
            ]
        }



# --- DEVICE REGISTER RESPONSE ---
class DeviceRegisterResponse(DeviceRegister):

    id: int

    class Config:
        orm_mode = True
        from_attributes = True
        use_enum_values = True


# Common configuration across devices
class BaseDeviceSchema(BaseModel):

    id: int
    device_id: str
    timestamp: datetime

    class Config:
        orm_mode = True
        from_attributes = True


class SmartLight(BaseDeviceSchema):

    status: SmartLightStatus

    
# --- THERMOSTATS ---
class Thermostat(BaseDeviceSchema):
    temperature: int
    humidity: int


# --- SECURITY CAMERAS ---
class SecurityCamera(BaseDeviceSchema):

    status: SecurityCameraStatus

    # class Config:
    #     from_attributes = True
    #     use_enum_values = True

class SecurityCameraDetails(BaseModel):
    device: DeviceRegisterResponse
    security_camera: Optional[SecurityCamera] = None

    class Config:
        orm_mode = True
        from_attributes = True
        use_enum_values = True