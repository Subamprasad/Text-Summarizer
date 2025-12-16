from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline
import uvicorn
import os
from fastapi import Request
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class TextIn(BaseModel):
    text: str

@app.get("/", tags=["authentication"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.post("/predict")
async def predict_route(text_in: TextIn):
    try:
        obj = PredictionPipeline()
        text = text_in.text
        summary = obj.predict(text)
        return summary
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
