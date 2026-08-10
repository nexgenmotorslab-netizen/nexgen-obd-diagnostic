from fastapi import FastAPI

app = FastAPI(title="NexGen MotorsLab OBD", version="1.0.0")

@app.get("/")
def home():
    return {"message": "NexGen MotorsLab OBD API is running "}

@app.get("/health")
def health():
    return {"status": "OK", "connected": car_conn.is_connected()}

@app.get("/rpm")
def rpm()
    if not car_conn.is_connect

