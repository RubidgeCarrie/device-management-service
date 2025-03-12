from fastapi import FastAPI

from app.routes.device_register import device_router, devices_router

app = FastAPI(title="IoT Device Management API", version="1.0")

CURRENT_API_VERSION = "/v1"

app.include_router(device_router, prefix=CURRENT_API_VERSION)
app.include_router(devices_router, prefix=CURRENT_API_VERSION)




@app.get("/")
async def root():
    return {"message": "Welcome to the IoT Device Management API!"}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
