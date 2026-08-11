from fastapi import FastAPI

app = FastAPI(
    title="JobPilot API",
    description="AI-powered job discovery and application tracking platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to JobPilot API",
        "status": "running"
    }