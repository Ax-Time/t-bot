import logging
import dotenv
import os
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Load environment variables
dotenv.load_dotenv()

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello, World!'}
