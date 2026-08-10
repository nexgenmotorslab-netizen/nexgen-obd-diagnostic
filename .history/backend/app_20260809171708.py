from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scanner import connect_to_car, get_rpm, get_speed, get_coolant_temp, get_engine_load, get_throttle, clear_dtc_codes
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

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

@app.get("/health")
def health():
    connected = car_conn.is_connected() if car_conn else False
    return {"status": "ok", "connected": connected}

@app.get("/rpm")
def rpm():
    if not car_conn or not car_conn.is_connected():
        return {"error": "Not connected to car"}
    return {"rpm": str(get_rpm(car_conn))}

@app.get("/speed")
def speed():
    if not car_conn or not car_conn.is_connected():
        return {"error": "Not connected to car"}
    return {"speed_kmh": str(get_speed(car_conn))}

@app.get("/coolant")
def coolant():
    if not car_conn or not car_conn.is_connected():
        return {"error": "Not connected to car"}
    return {"coolant_temp_c": str(get_coolant_temp(car_conn))}

@app.get("/load")
def engine_load():
    if not car_conn or not car_conn.is_connected():
        return {"error": "Not connected to car"}
    return {"engine_load_percent": str(get_engine_load(car_conn))}

@app.get("/throttle")
def throttle():
    if not car_conn or not car_conn.is_connected():
        return {"error": "Not connected to car"}
    return {"throttle_percent": str(get_throttle(car_conn))}


    @app.get("/faults")
def get_faults():
    """Detects all sensors at fault. Returns DTC codes like P0301"""
    if not car_conn or not car_conn.is_connected():
        return {"error": "Not connected to car"}
    
    codes = get_dtc_codes(car_conn)
    if not codes:
        return {"status": "OK", "faults": "No fault codes found"}
    
    return {"status": "FAULTS FOUND", "faults": [str(code) for code in codes]}


@app.post("/reset")
def reset_sensors():
    """Clears ALL fault codes and resets Engine Light"""
    if not car_conn or not car_conn.is_connected():
        return {"error": "Not connected to car"}
    
    result = clear_dtc_codes(car_conn)
    if result.is_null():
        return {"status": "FAILED", "message": "Could not clear codes"}
    
    return {"status": "SUCCESS", "message": "All faults cleared. Engine light reset"}