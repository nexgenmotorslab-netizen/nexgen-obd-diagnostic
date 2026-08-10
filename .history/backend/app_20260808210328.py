from fastapi import FastAPI

app = FastAPI(title="NexGen MotorsLab OBD", version="1.0.0")

@app.get("/")
def home():
    return {"message": "NexGen MotorsLab OBD API is running "}

@app.get("/health")
def health():
    return {"status": "OK" }

