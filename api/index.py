from fastapi import FastAPI
from telegram import Update, Bot
import dotenv
import os

dotenv.load_dotenv()

app = FastAPI()
bot = Bot(os.environ.get("TOKEN"))

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/updates")
async def handle_update(update: dict):
    update = Update.de_json(update, bot)
    return {"update": update}