import logging
import dotenv
import os
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Load environment variables
dotenv.load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
 
# Initialize the Telegram bot application
telegram_app = Application.builder().token(os.getenv("TOKEN")).build()

# Define command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=None,
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

# Add handlers to the Telegram application
telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("help", help_command))
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Create the FastAPI app
app = FastAPI()

# Webhook endpoint
@app.post("/api/index")
async def webhook(request: Request):
    """Handle incoming Telegram updates."""
    json_data = await request.json()
    update = Update.de_json(json_data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"status": "ok"}

# Start the Telegram webhook
@app.on_event("startup")
async def startup():
    webhook_url = os.getenv("DOMAIN") + "/api/index"
    await telegram_app.bot.set_webhook(webhook_url)

@app.on_event("shutdown")
async def shutdown():
    await telegram_app.bot.delete_webhook()
