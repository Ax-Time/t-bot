from telegram import Update
from abc import abstractmethod
from typing import Any

class Handler:
    @abstractmethod
    def check(self, update: Update) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def handle(self, update: Update) -> None:
        raise NotImplementedError()

def is_command(update: Update, cmd: str | Any = None) -> bool:
    try:
        return update.message.text.startswith("/") and (cmd is None or update.message.text == f'/{cmd}')
    except AttributeError:
        return False