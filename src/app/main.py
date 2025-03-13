from fastapi import FastAPI

from app.routes import device_router, devices_router, security_camera_router

app = FastAPI(title="IoT Device Management API", version="1.0")

CURRENT_API_VERSION = "/v1"

app.include_router(device_router, prefix=CURRENT_API_VERSION)
app.include_router(devices_router, prefix=CURRENT_API_VERSION)
app.include_router(security_camera_router, prefix=CURRENT_API_VERSION)


@app.get("/")
async def root():
    return {"message": "Welcome to the IoT Device Management API!"}
