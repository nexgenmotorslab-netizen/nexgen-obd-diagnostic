from filecmp import dircmp
import os
import importlib.util
from typing import ModuleType
from fastapi import FastAPI


# Load scanner.py from the obd folder 
current_dir = os.path.dirname(os.path.abspath(___file___))
scanner_path = os.path.join(current_dir, "..", "obd", "scanner.py")

spec = importlibutil.
obd_scanner: ModuleType = importlib.util.module_from_spec(spec)
spec.loader.exec_module(obd_scanner)
 

connect_to_car = obd_scanner.connect_to_car
get_rpm = obd_scanner.get_rpm

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
