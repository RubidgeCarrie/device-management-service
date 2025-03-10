import enum
import uuid
from datetime import datetime
from enum import Enum
from ipaddress import IPv4Address
from typing import Any, Dict, Literal, Type

from pydantic import IPvAnyAddress
from sqlalchemy import UUID, Boolean, Column, DateTime
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ENUM, INET, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()

DeviceTypes = Literal["smart_light", "thermostat", "security_camera"]

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    username: Mapped[str] = mapped_column(index=True, unique=True)
    slug: Mapped[str] = mapped_column(index=True, unique=True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    hashed_password: Mapped[str]
    is_superuser: Mapped[bool] = mapped_column(default=False)


# Enums




class DeviceStatus(Enum):
    ON = 1
    OFF = 0

DEVICE_STATUS = Literal[0, 1]

class SmartLightStatus(str, Enum):
    ON = "on"
    OFF = "off"


class SecurityCameraStatus(str, Enum):
    ARMED = "armed"
    DISARMED = "disarmed"


# Device Registration
class DeviceRegister(Base):
    """Stores immutable/ long lived configuration for devices"""

    __tablename__ = "device_register"

    # id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_type: Mapped[DeviceTypes] = mapped_column(nullable=False)
    # ip_address = Mapped[INET] = mapped_column(nullable=False)
    registration_date: Mapped[datetime] = mapped_column(nullable=False)


# Device specific configuration and status updates
class BaseDevice(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id", ondelete="CASCADE"), index=True)
    timestamp: Mapped[datetime] = mapped_column(nullable=False)


class SmartLights(BaseDevice):
    __tablename__ = "smart_lights"

    status: Mapped[DEVICE_STATUS] = mapped_column(nullable=False)


# class Thermostats(BaseDevice):
#     __tablename__ = "thermostats"

#     temperature: Mapped[int] = mapped_column(Integer)
#     humidity: Mapped[int] = mapped_column(Integer)


# class SecurityCameras(BaseDevice):
#     __tablename__ = "security_cameras"

#     status: Mapped[SecurityCameraStatus] = mapped_column(ENUM(SecurityCameraStatus, name="security_camera_status"), nullable=False)