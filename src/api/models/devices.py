from enum import Enum
from ipaddress import IPv4Address
from datetime import datetime
from typing import Any, Dict, Type
from sqlalchemy import (
    Column, Integer, String, Boolean, ForeignKey, DateTime, Enum as SQLEnum
)
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



# Enums
class DeviceTypes(str, Enum):
    SMART_LIGHTS = "smart_lights"
    THERMOSTATS="thermostats"
    SECURITY_CAMERAS = "secuirty_cameras"

class DeviceStatus(Enum):
    ON = 1
    OFF = 0

class SmartLightStatus(str, Enum): 
    ON = "on"
    OFF = "off"

class SecurityCameraStatus(str, Enum): 
    ARMED = "armed"
    DISARMED = "disarmed"

# Device Registration
class DeviceRegister(Base):
    """Stores immutable/ long lived configuration for devices"""
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_type = Column(SQLEnum(DeviceTypes), nullable=False) 
    ip_address = Column(INET, nullable=False) 
    registration_date = Column(DateTime, default=datetime.utcnow)

# Device specific configuration and status updates
class BaseDevice(Base):
    __abstract__ = True 

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey("devices.id", ondelete="CASCADE"), index=True)
    is_online = Column(Boolean, nullable=False, default=True)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SmartLights(BaseDevice):
    __tablename__ = "smart_lights"

    status = Column(SQLEnum(SmartLightStatus), nullable=False) 

class Thermostats(BaseDevice):
    __tablename__ = "thermostats"

    temperature = Column(Integer)
    humidity = Column(Integer)

class SecurityCameras(BaseDevice):
    __tablename__ = "security_cameras"

    status = Column(SQLEnum(SecurityCameraStatus), nullable=False) 


DEVICE_TYPE_MODEL_MAP: dict[str, Any] = {
    DeviceTypes.SMART_LIGHTS.value: SmartLights,
    "thermostat": Thermostats,  # Add enum values as needed
    "security_camera": SecurityCameras
}