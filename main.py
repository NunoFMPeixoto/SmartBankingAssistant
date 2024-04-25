from fastapi import FastAPI
from app.routers import v1

app = FastAPI()

app.include_router(v1.router, prefix="/v1", tags=["v1"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Intention Classifier API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)