# device-management-service
Handles device management for IoT devices
```bash
docker compose up device_db
```
```bash
docker-compose up device-api
```

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

## File Structure 
.
├── app
│   ├── __init__.py
│   └── main.py
├── Dockerfile
└── requirements.txt


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


https://github.com/ThomasAitken/demo-fastapi-async-sqlalchemy/blob/main/backend/app/models/__init__.py

https://github.com/tzelleke/fastapi-sqlalchemy/blob/main/app/core/config.py

https://medium.com/@tclaitken/setting-up-a-fastapi-app-with-async-sqlalchemy-2-0-pydantic-v2-e6c540be4308

scripts/migrate.py file.

import asyncio
import logging

from sqlalchemy.ext.asyncio import create_async_engine

from alchemist.config import settings
from alchemist.database.models import Base

logger = logging.getLogger()


async def migrate_tables() -> None:
    logger.info("Starting to migrate")

    engine = create_async_engine(settings.DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Done migrating")


if __name__ == "__main__":
    asyncio.run(migrate_tables())



https://dev.to/devasservice/fastapi-best-practices-a-condensed-guide-with-examples-3pa5

For a PUT request: HTTP 200, HTTP 204 should imply "resource updated successfully". HTTP 201 if the PUT request created a new resource.

For a DELETE request: HTTP 200 or HTTP 204 should imply "resource deleted successfully".

HTTP 202 can also be returned by either operation and would imply that the instruction was accepted by the server, but not fully applied yet. It's possible that the operation fails later, so the client shouldn't fully assume that it was success.

A client that receives a status code it doesn't recognize, but it's starting with 2 should treat it as a 200 OK.

PUT

If an existing resource is modified, either the 200 (OK) or 204 (No Content) response codes SHOULD be sent to indicate successful completion of the request.

DELETE

A successful response SHOULD be 200 (OK) if the response includes an entity describing the status, 202 (Accepted) if the action has not yet been enacted, or 204 (No Content) if the action has been enacted but the response does not include an entity.

Create IoT Device Management API:

Register a New Device: 

List All Devices: Get all devices from static details table

Get Device Details: Get device with its latest status

Update Device Status: Add new device status

Delete a Device: 
