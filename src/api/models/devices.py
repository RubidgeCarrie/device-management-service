from enum import Enum
from ipaddress import IPv4Address
from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Boolean, ForeignKey, DateTime, Enum as SQLEnum
)
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Enums
class DeviceTypes(str, Enum):  # FIXED: Proper Enum definition
    SMART_LIGHTS = "smart_lights"
    THERMOSTATS="thermostats"
    SECURITY_CAMERAS = "secuirty_cameras"

class DeviceStatus(Enum):  # FIXED: Changed to SQL-compatible Enum
    ON = 1
    OFF = 0

class SmartLightStatus(str, Enum):  # FIXED: Converted to proper Enum
    ON = "on"
    OFF = "off"

class SecurityCameraStatus(str, Enum):  # FIXED: Converted to proper Enum
    ARMED = "armed"
    DISARMED = "disarmed"

# Devices Table
class Devices(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_type = Column(SQLEnum(DeviceTypes), nullable=False)  # FIXED: Proper ENUM usage
    ip_address = Column(INET, nullable=False)  # FIXED: Use INET type for IP addresses
    is_online = Column(Boolean, nullable=False)

# Smart Lights Table
class SmartLights(Base):
    __tablename__ = "smart_lights"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey("devices.id", ondelete="CASCADE"), index=True)  # FIXED: Add CASCADE delete
    last_updated = Column(DateTime, default=datetime.utcnow)  # FIXED: Correct DateTime usage
    status = Column(SQLEnum(SmartLightStatus))  # FIXED: Use ENUM instead of list

# Thermostats Table
class Thermostats(Base):
    __tablename__ = "thermostats"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey("devices.id", ondelete="CASCADE"), index=True)  # FIXED: Add CASCADE delete
    last_updated = Column(DateTime, default=datetime.utcnow)  # FIXED: Correct DateTime usage
    temperature = Column(Integer)
    humidity = Column(Integer)

# Security Cameras Table
class SecurityCameras(Base):
    __tablename__ = "security_cameras"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey("devices.id", ondelete="CASCADE"), index=True)  # FIXED: Add CASCADE delete
    last_updated = Column(DateTime, default=datetime.utcnow)  # FIXED: Correct DateTime usage
    status = Column(SQLEnum(SecurityCameraStatus))  # FIXED: Use ENUM instead of list
