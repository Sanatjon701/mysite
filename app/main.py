from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/robots.txt", response_class=FileResponse)
async def robots():
    return "app/templates/robots.txt"

@app.get("/sitemap.xml", response_class=FileResponse)
async def sitemap():
    return "app/templates/sitemap.xml"