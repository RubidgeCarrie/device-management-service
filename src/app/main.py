import sys

from fastapi import FastAPI

from app.routes.devices import router as devices_router  # Import your router

app = FastAPI(title="AICO Device Management API", version="1.0")

# Include the devices router
app.include_router(devices_router, prefix="/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to the AICO Device Management API!"}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
