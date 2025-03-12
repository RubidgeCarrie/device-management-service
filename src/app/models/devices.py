import enum
from datetime import datetime
from typing import Literal

from sqlalchemy import Enum as SQLEmun
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


DeviceTypes = Literal["smart_light", "thermostat", "security_camera"]

SecurityCameraStatus = Literal["armed", "disarmed", "alarm", "off"]
ThermostatStatus = Literal["on", "off"]
SmartLightStatus = Literal["on", "off"]


class DeviceRegister(Base):
    """Stores device details. These are immutable/ long-lived attributes."""

    __tablename__ = "device_register"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_type: Mapped[DeviceTypes] = mapped_column(nullable=False)
    ip_address: Mapped[str] = mapped_column(INET, nullable=False) 
    mac_address: Mapped[str] = mapped_column(String(17), nullable=True, unique=True)
    registration_date: Mapped[datetime] = mapped_column(nullable=False)



#----------------
    # Historic status/ configuration 
#----------------


class BaseDevice(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_id: Mapped[int] = mapped_column(
        ForeignKey("devices.id", ondelete="CASCADE"), index=True
    )
    timestamp: Mapped[datetime] = mapped_column(nullable=False, index=True)

    
class SmartLights(BaseDevice):
    __tablename__ = "smart_lights"

    status: Mapped[SmartLightStatus]


class Thermostats(BaseDevice):
    __tablename__ = "thermostats"

    status: Mapped[ThermostatStatus]
    temperature: Mapped[int] = mapped_column(Integer)
    humidity: Mapped[int] = mapped_column(Integer)


class SecurityCamera(BaseDevice):
    __tablename__ = "security_cameras"

    status: Mapped[SecurityCameraStatus] = mapped_column()

# if __name__ == "__mi"
