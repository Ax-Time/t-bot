from api.commands import core
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class StartCommand(core.Handler):
    def check(self, update) -> bool:
        return core.is_command(update, 'start')
    
    async def handle(self, update) -> None:
        await update.message.reply_text('Hello! I am ready.')