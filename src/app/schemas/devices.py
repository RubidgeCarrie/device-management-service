from datetime import datetime
from typing import Optional

from pydantic import BaseModel, IPvAnyAddress

from app.models.devices import (DeviceTypes, SecurityCameraStatus,
                                ThermostatStatus)

#-----------------------------------
    # Device registry (device summary)
#-----------------------------------

class DeviceRegister(BaseModel):
    device_type: DeviceTypes
    ip_address: IPvAnyAddress
    mac_address: Optional[str] = None
    registration_date: datetime

    class Config:
        from_attributes = True
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



class DeviceRegisterResponse(DeviceRegister):
    id: int

    class Config:
        from_attributes = True

#-----------------------------------
    # Status/ configuration history
#-----------------------------------

class BaseDeviceSchema(BaseModel):
    device_id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# --------------
#  Thermostats
# --------------
    
class Thermostat(BaseDeviceSchema):
    status: ThermostatStatus
    temperature: int
    humidity: int

class ThermostatResponse(Thermostat):
    id: int

class ThermostatDetails(BaseDeviceSchema):
    summary: DeviceRegisterResponse
    status: Optional[ThermostatResponse] = None

# --------------
#  Security Cameras
# --------------
        
class SecurityCamera(BaseDeviceSchema):
    status: SecurityCameraStatus

    class Config:
        from_attributes = True
        json_schema_extra = {
  "device_id": 3,
  "timestamp": "2025-03-13T07:54:30.772Z",
  "status": "armed"
}


class SecurityCameraResponse(SecurityCamera):
    id: int

class SecurityCameraDetails(BaseModel):
    summary: DeviceRegisterResponse
    status: Optional[SecurityCameraResponse] = None