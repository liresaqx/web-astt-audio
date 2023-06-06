import wave
import datetime
from tempfile import NamedTemporaryFile
from typing import Union

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from pydub import AudioSegment

app = FastAPI()
templates = Jinja2Templates(directory="fastapienv/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_video(media:UploadFile = File(...)):
    return {"filename": media.filename}
