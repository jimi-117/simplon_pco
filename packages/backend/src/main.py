from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class PredictRequest(BaseModel):
    data: str

class PredictResponse(BaseModel):
    result: str

@app.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    # Dummy prediction logic
    if not request.data:
        raise HTTPException(status_code=400, detail="Invalid input data")
    
    # Return dummy prediction result
    return PredictResponse(result="dummy_result")

@app.get("/status")
async def status():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)