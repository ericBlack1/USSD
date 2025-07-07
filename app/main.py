from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from app.ussd_handler import handle_ussd
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.post("/ussd", response_class=PlainTextResponse)
async def ussd_callback(
    sessionId: str = Form(...),
    serviceCode: str = Form(...),
    phoneNumber: str = Form(...),
    text: str = Form("")
):
    response = handle_ussd(sessionId, phoneNumber, text)
    return response

