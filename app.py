from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from TextSummarizer.pipeline.prediction import Prediction

text:str="What is text summarization?"

app=FastAPI()

@app.get("/",tags=["authentication"]) #default route
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")#Any command written here will be executed
        return Response("Training Successful")
    
    except Exception as e:
        return Response(f"Error Occured!{e}")
    


@app.post("/predict")
async def predict_route(text):
    try:
        obj=Prediction()
        text=obj.predict(text)
        return text
    except Exception as e:
        raise e    
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) #Initialising the host and port to run this FastAPI app   