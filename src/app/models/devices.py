import enum
from datetime import datetime
from typing import Literal

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


# -----------------------------------
# Device registry (device summary)
# -----------------------------------

DeviceTypes = Literal["smart_light", "thermostat", "security_camera"]


class DeviceTypesEnum(enum.StrEnum):
    SMART_LIGHT = "smart_light"
    THERMOSTAT = "thermostat"
    SECURITY_CAMERA = "security_camera"


class DeviceRegister(Base):
    """Stores device details. These are immutable/ long-lived attributes."""

    __tablename__ = "device_register"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_type: Mapped[DeviceTypes] = mapped_column(nullable=False)
    ip_address: Mapped[str] = mapped_column(INET, nullable=False)
    mac_address: Mapped[str] = mapped_column(String(17), nullable=True, unique=True)
    registration_date: Mapped[datetime] = mapped_column(nullable=False)


# -----------------------------------
# Status/ configuration history
# -----------------------------------

SecurityCameraStatus = Literal["armed", "disarmed", "alarm", "off"]
ThermostatStatus = Literal["on", "off"]


class BaseDevice(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_id: Mapped[int] = mapped_column(
        ForeignKey("device_register.id", ondelete="CASCADE"), index=True
    )
    timestamp: Mapped[datetime] = mapped_column(nullable=False, index=True)


class Thermostat(BaseDevice):
    __tablename__ = "thermostats"

    status: Mapped[ThermostatStatus]
    temperature: Mapped[int]
    humidity: Mapped[int]


class SecurityCamera(BaseDevice):
    __tablename__ = "security_cameras"

    status: Mapped[SecurityCameraStatus]
