from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scanner import connect_to_car, get_rpm, get_speed, get_coolant_temp, get_engine_load, get_throttle

app = FastAPI(title="NexGen MotorsLab OBD API v2")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Connecting to OBD...")
car_conn = connect_to_car()

@app.get("/")
def home():
    return {"message": "NexGen MotorsLab OBD API v2 is running"}

