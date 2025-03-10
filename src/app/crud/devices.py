from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from app.models.devices import DeviceRegister as DeviceRegisterModel
from app.models.devices import User as UserDBModel


def get_user_by_id(db_session: Session, user_id: int):
    """Fetches a user by ID synchronously."""
    user = db_session.query(UserDBModel).filter(UserDBModel.id == user_id).first()

    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")

    return user


def get_device_by_id(db_session: Session, device_id: int):
    """Fetches a device from the device register"""
    device = (
        db_session.query(DeviceRegisterModel)
        .filter(DeviceRegisterModel.id == device_id)
        .first()
    )

    if not device:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Device not found")

    return device


def delete_device_by_id(db_session: Session, device_id: int):
    """Deletes a device from the device register.

    The delete cascasde on the device_id will remove its status and historic data
    """
    device = (
        db_session.query(DeviceRegisterModel)
        .filter(DeviceRegisterModel.id == device_id)
        .first()
    )

    if not device:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Device not found")

    db_session.delete(device)
    db_session.commit()

    return {"message": "Device deleted successfully"}