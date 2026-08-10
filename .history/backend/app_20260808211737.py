from fastapi import FastAPI
import sys
import os

# THIS LETS US IMPORT FROM THE OBD FOLDER
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from obd.scanner import connect_to_car, get_rpm

app = FastAPI(title="NexGen MotorsLab OBD", version="1.0.0")

car_conn = None

@app.on_event("startup")
def startup_event():
    global car_conn
    car_conn = connect_to_car()


@app.get("/")
def home():
    return {"message": "NexGen MotorsLab OBD API is running "}


@app.get("/health")
def health():
    connected = car_conn.is_connected() if car_conn else False
    return {"status": "OK", "connected": connected}


@app.get("/rpm")
def rpm():
    if not car_conn or not car_conn.is_connected():
        return {"error": "Not connected to car"}
    rpm_value = get_rpm(car_conn)
    return {"rpm": str(rpm_value)}
