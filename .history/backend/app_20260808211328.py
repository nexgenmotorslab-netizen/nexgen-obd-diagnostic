from fastapi import FastAPI
import sys
import os 

# THIS LET US IMPORT FROM THE OBD FOLDER 
sys,path.append(os,path,dirname(os,path.dirname(os.)))
app = FastAPI(title="NexGen MotorsLab OBD", version="1.0.0")

# Initialize car connection
car_conn = None


def get_rpm(connection):
    return connection.get_rpm()


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
