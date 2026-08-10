import importlib.util
import os

from fastapi import FastAPI

current_dir = os.path.dirname(os.path.abspath(__file__))
scanner_path = os.path.join(current_dir, "obd", "scanner.py")
spec = importlib.util.spec_from_file_location("obd_scanner", scanner_path)
if spec is None or spec.loader is None:
    raise ImportError(f"Cannot load scanner module from {scanner_path}")
obd_scanner = importlib.util.module_from_spec(spec)
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
