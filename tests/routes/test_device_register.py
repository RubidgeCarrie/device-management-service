"""
Integration tests for Device Registration routes

Could be improved with fixtures to handle insertion/ removal of data before and after tests
"""
from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app.main import CURRENT_API_VERSION, app
from src.app.schemas import DeviceRegister, DeviceRegisterResponse

# Test client setup
client = TestClient(app)


class TestListDevices:
    """Test List devices route"""

    def test_list_devices(self):
        response = client.get(f"{CURRENT_API_VERSION}/devices/")
        assert response.status_code == HTTPStatus.ACCEPTED
        assert isinstance(response.json(), list)  # Expecting list of devices


class TestRegisterDevice:
    """Test register device with valid data"""

    def test_register_device(self):
        """Test correct device registration"""
        # Arrange
        device_data = {
            "device_type": "security_camera",
            "ip_address": "192.168.1.10",
            "registration_date": "2025-03-13T00:00:00",
            "mac_address": "00-B0-D0-63-C2-27",
        }

        # Act
        response = client.post(f"{CURRENT_API_VERSION}/devices/", json=device_data)

        # Assert
        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.json()["id"], int)
        assert response.json()["ip_address"] == device_data["ip_address"]
        assert response.json()["device_type"] == device_data["device_type"]

    def test_register_device_invalid_data(self):
        """Test invalid device body fails"""
        # Arrange post with invalid ip_address
        device_data = {
            "device_type": "security_camera",
            "ip_address": "invalid_ip",
            "registration_date": "2025-03-13T00:00:00",
            "mac_address": "00-B0-D0-63-C2-29",
        }
        # Act
        response = client.post(f"{CURRENT_API_VERSION}/devices/", json=device_data)

        # Assert: Expecting validation error due to invalid IP address
        assert response.status_code == HTTPStatus.UNPROCESSABLE_CONTENT


class TestDeleteDevices:
    """Test delete devices"""

    # TODO: Expand this to confirm delete cascade works to remove data from relevant status table
    def test_delete_device(self):
        """Test successful delete"""
        # Arrange
        device_data = {
            "device_type": "security_camera",
            "ip_address": "192.168.1.11",
            "registration_date": "2025-03-13T00:00:00",
            "mac_address": "00-B0-D0-63-C2-28",
        }
        register_response = client.post(
            f"{CURRENT_API_VERSION}/devices/", json=device_data
        )
        device_id = register_response.json()["id"]

        # Act
        response = client.delete(f"{CURRENT_API_VERSION}/device/{device_id}")

        # Assert: Expecting no content response (successful deletion)
        assert response.status_code == HTTPStatus.NO_CONTENT

    def test_delete_non_existing_device(self):
        """Test non existent device id gives 404 on delete attempt"""
        # Arrange
        # Assuming this ID does not exist in the database (and we are using a test bd we setup)
        non_existing_device_id = 9999

        # Act
        response = client.delete(
            f"{CURRENT_API_VERSION}/device/{non_existing_device_id}"
        )

        assert response.status_code == HTTPStatus.NOT_FOUND
