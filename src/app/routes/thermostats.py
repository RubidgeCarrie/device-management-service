# Get Device Details:

from fastapi import APIRouter

thermostats_router = APIRouter(
    prefix="/thermostat",
    tags=["Security Cameras"],
    responses={404: {"description": "Not found"}},
)