from fastapi import FastAPI
import os
from dotenv import load_dotenv
from typing import Optional
import telegram

load_dotenv()
TOKEN = os.environ.get('TOKEN')
app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.post('/webhook')
def webhook(webhook_data):
    print(webhook_data)