# device-management-service
Handles device management for IoT devices

## Getting Started

### Dependencies
* Docker Engine - https://docs.docker.com/engine/install/
* Docker Compose - https://docs.docker.com/compose/install/


### Run With Docker
You must have ```docker``` and ```docker-compose``` tools installed to work with material in this section.
Head to the ```/src``` folder of the project.
To run the program, we spin up the containers with
```
docker-compose up
```
If this is the first time bringing up the project, you need to build the images first:
```
docker-compose up --build
```

Create IoT Device Management API:

# Register a New Device:

Create an endpoint to register a new IoT device. The API should accept the necessary details to uniquely identify and describe the device.
The response should return the details of the registered device, including a unique identifier.
List All Devices:

Implement an endpoint to retrieve a list of all registered devices. This endpoint should return a summary of each device's details.

# Get Device Details:

Create an endpoint to retrieve the details of a specific device by its unique identifier.

# Update Device Status:

Provide an endpoint to update the status or configuration of a specific device. This could be used, for example, to turn a light on or off, adjust a thermostat, etc.
The response should confirm the updated status or configuration.

# Delete a Device:

Implement an endpoint to delete a specific device from the system. The response should confirm the deletion.

... /v1 / device/
post -> registar a new device with device body 


https://github.com/tzelleke/fastapi-sqlalchemy/blob/main/app/core/config.py