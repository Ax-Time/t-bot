from fastapi import FastAPI
from telegram import Update, Bot
import dotenv
import os
from typing import List

from api.commands.core import Handler
from api.commands.start import StartCommand

dotenv.load_dotenv()

app = FastAPI()
bot = Bot(token=os.environ.get("TOKEN"))

def is_start(update: Update):
    try:
        return update.message.text == "/start"
    except AttributeError:
        return False

async def start(update: Update):
    await update.message.reply_text("Hello, World!")

handlers: List[Handler] = [
    StartCommand(),
]

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.post("/updates")
async def handle_update(update: dict):
    update: Update = Update.de_json(update, bot)
    for handler in handlers:
        if handler.check(update):
            await handler.handle(update)
    
# Run the server
# uvicorn api.index:app --reload
