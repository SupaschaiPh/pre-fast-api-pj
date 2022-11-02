from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os

app = FastAPI()
tem = Jinja2Templates(directory=__file__[:__file__.rfind("\\")].replace("\\", "/")+"/tem")
gb_name = ""

@app.get("/{name}",response_class=RedirectResponse)
async def home(req:Request,name):
    global gb_name 
    gb_name = name
    return RedirectResponse(app.url_path_for("index"))

@app.get("/",response_class=HTMLResponse)
async def index(req:Request):
    global gb_name
    return tem.TemplateResponse("home.html", {"request":req,"name":gb_name})
uvicorn.run(app,port=2222)
