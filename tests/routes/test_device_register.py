"""
Integration tests for 
"""
from fastapi import HTTPException
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.connection import get_device_db
from app.main import app  # Assuming your FastAPI app is in app.main
from app.schemas import DeviceRegister, DeviceRegisterResponse

# Test client setup
client = TestClient(app)


# this would be replaced with a test DB
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@device_db:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency override to use the test database
def override_get_device_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Replace the dependency in the app with the test database dependency
app.dependency_overrides[get_device_db] = override_get_device_db


# Test Register Device API
def test_register_device():
    device_data = {
        "device_type": "security_camera",
        "ip_address": "192.168.1.10",
        "registration_date": "2025-03-13T00:00:00",
        "mac_address": "00-B0-D0-63-C2-27"
    }

    response = client.post("/devices/", json=device_data)

    assert response.status_code == 200  # Expecting success status code
    assert response.json()["ip_address"] == device_data["ip_address"]
    assert response.json()["device_type"] == device_data["device_type"]


# Test List Devices API
def test_list_devices():
    response = client.get("/devices/")

    assert response.status_code == 202  # Expecting accepted status code
    assert isinstance(response.json(), list)  # Expecting list of devices


# Test Delete Device API
def test_delete_device():
    # First register a device to delete it
    device_data = {
        "device_type": "security_camera",
        "ip_address": "192.168.1.11",
        "registration_date": "2025-03-13T00:00:00",
        "mac_address": "00-B0-D0-63-C2-28"
    }
    register_response = client.post("/devices/", json=device_data)
    device_id = register_response.json()["id"]  # Get the ID of the newly registered device

    # Now delete the device
    response = client.delete(f"/device/{device_id}")

    assert response.status_code == 204  # Expecting no content response (successful deletion)


# Test Register Device with Invalid Data
def test_register_device_invalid_data():
    device_data = {
        "device_type": "security_camera",
        "ip_address": "invalid_ip",
        "registration_date": "2025-03-13T00:00:00",
        "mac_address": "00-B0-D0-63-C2-29"
    }

    response = client.post("/devices/", json=device_data)

    assert response.status_code == 422  # Expecting validation error due to invalid IP address
    assert "value is not a valid ip address" in response.text


# Test Delete Non-Existing Device
def test_delete_non_existing_device():
    non_existing_device_id = 9999  # Assuming this ID does not exist in the database
    response = client.delete(f"/device/{non_existing_device_id}")

    assert response.status_code == 404  # Expecting device not found error


