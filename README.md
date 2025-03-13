#  IoT Device Management API:

This service managed IoT devices. It includes a postgres database and API's for interacting with the device details.

![OpenAPI](/docs/openapi.png)

It makes use of:
[FastAPI](https://fastapi.tiangolo.com/): Web framework for building APIs with Python   \
[SQLAlchemy](https://www.sqlalchemy.org/): ORM for python  \
[Pydantic](https://docs.pydantic.dev/latest/): Model Validation, integrates well with FastAPi for swagger documentation \

## Getting Started

### Dependencies
* Docker Engine - https://docs.docker.com/engine/install/
* Docker Compose - https://docs.docker.com/compose/install/

### Run With Docker
You must have ```docker``` and ```docker-compose``` tools installed to work with material in this section.
Head to the ```/src``` folder of the project.

If this is the first time bringing up the project, you need to build the images first:
```
docker-compose up --build
```

To run the program, we spin up the containers with
```
docker compose up device_db
docker-compose up device-api
```

You can then access openAPI doc at `http://0.0.0.0:8000/docs#/` which has example requests. \

The OpenAPI `yaml` file is also saved in [openapi.yaml](openapi.yaml) but due to conversion the above is preferential.

## File Structure 

```bash
├── docs # A brief summary of approach, improvements and challenges
├── README.md # Instructions on running and challenges
├── src
│   ├── app
│   │   ├── connection.py
│   │   ├── crud 
│   │   ├── main.py # API Main
│   │   ├── models # SQLAlchemy ORM models
│   │   │   ├── devices.py
│   │   ├── routes # FastAPI Routes
│   │   │   ├── device_register.py
│   │   │   ├── security_cameras.py
│   │   │   └── thermostats.py
│   │   └── schemas # Pydantic Schemas
│   │       ├── devices.py
│   ├── device_db # Postgres Database
│   │   └── init.sql
│   ├── Dockerfile
│   └── requirements.txt
├── tests
├── docker-compose.yaml
```

## Assumptions

1. We would like to save both device summaries (long-lived/immutable attributes) and their status history
2. We want to save the history of a device status/configuration changes

## API Summary

**Device summary**: Long-lived/immutable attributes of device \
**Device status**: Configuration settings for device \
**Device details**: All information about a device, including static attributes

The following API's are available:

1. **Register a New Device:** 
    -  `POST` `/devices`
    - Registers device details
2. **List all Devices**
    - `GET` `/devices`
    -  Returns all devices with a summary of their details
3. **Get Device Details:**
    - On a per device type route
    - `GET` `/security-camera/{device_id}`
    - Returns all details
4. **Update Device Status:**
    - On a per device type route
        - `POST` `/security-camera`
        - Adds latest security camera status to history
5. **Delete a Device**
    - `DELETE` `/device/{device_id}`
    - Deletes device from Registry and all status history

## Testing
Integration tests have been setup for the routes, running against the postgres database (after standing up device_db), run:

```bash
docker compose build tests 
docker compose run tests
```
