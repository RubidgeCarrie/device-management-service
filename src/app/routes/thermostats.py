from http import HTTPStatus

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

import app.schemas as schemas
from app.connection import get_device_db
from app.crud.thermostats import get_thermostat_by_id

thermostat_router = APIRouter(
    prefix="/thermostat",
    tags=["Thermostats"],
    responses={404: {"description": "Not found"}},
)

# Get Device Details:
@thermostat_router.get(
    "/{device_id}",
    response_model= schemas.ThermostatDetails,
    status_code= HTTPStatus.ACCEPTED,
    summary="Retrieve the latest details/status for specified thermostat",
)
def get_thermostat(
    device_id: int = Path(
        description="Filter to only return status/configuration details for given thermostat"
    ),
    session: Session = Depends(get_device_db),
):
    """API route to fetch a device by ID."""
    return get_thermostat_by_id(session=session, device_id=device_id)

# Update Device Status:
# @thermostat_router.post(
#     "/",
#     status_code=HTTPStatus.OK,
#     response_model=schemas.DeviceRegisterResponse,
#     summary="Update thermostat device status",
# )
# def register_device(
#     device: schemas.DeviceRegister,
#     session: Session = Depends(get_device_db),
# ):
#     """API route to to update a thermostat status"""
#     return post_device(session=session, device=device)