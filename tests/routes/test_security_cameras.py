"""
Integration tests for Security Camera routes

Could be improved with fixtures to handle insertion/ removal of data before and after tests
"""
from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app.main import CURRENT_API_VERSION, app
from src.app.schemas import SecurityCamera, SecurityCameraResponse

# Test client setup
client = TestClient(app)


class TestGetSecurityCameras:
    """Test Get security camera details route"""

    def test_get_security_camera_details(self):
        """Test retrieving details for an existing security camera"""
        # Arrange: using known fake input data
        device_id = 3

        # Act
        response = client.get(f"{CURRENT_API_VERSION}/security-camera/{device_id}")
        print("response", response.json())

        assert response.status_code == HTTPStatus.ACCEPTED

    def test_get_non_existing_security_camera(self):
        """Test retrieving details for a non-existing security camera"""
        # Arrange
        non_existing_device_id = 9999  # Assume this device does not exist

        # Act
        response = client.get(
            f"{CURRENT_API_VERSION}/security-camera/{non_existing_device_id}"
        )

        assert response.status_code == HTTPStatus.NOT_FOUND


class TestUpdateStatus:
    """Test Update security camera status route"""

    def test_update_security_camera_status(self):
        """Test updating status for an existing security camera"""
        # Arrange
        # Assumes the database has been stood up with test data
        status_data = {
            "device_id": 3,
            "timestamp": "2025-03-13T12:25:10.352Z",
            "status": "armed",
        }

        # Act
        response = client.post(
            f"{CURRENT_API_VERSION}/security-camera/", json=status_data
        )

        # Assert
        assert response.status_code == HTTPStatus.OK

    def test_update_status_for_non_existing_security_camera(self):
        """Test updating status for a non-existing security camera"""
        # Arrange
        # Assume this device does not exist
        non_existing_device_id = 9999
        status_data = {
            "device_id": non_existing_device_id,
            "timestamp": "2025-03-13T12:25:10.352Z",
            "status": "armed",
        }

        # Act
        response = client.post(
            f"{CURRENT_API_VERSION}/security-camera/",
            json=status_data,
        )

        # Assert
        assert response.status_code == HTTPStatus.NOT_FOUND
