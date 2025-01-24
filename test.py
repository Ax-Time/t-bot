import telegram
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("TOKEN")

async def main():
    bot = telegram.Bot(TOKEN)
    async with bot:
        updates = (await bot.get_updates())[0]
        print(updates)

if __name__ == '__main__':
    asyncio.run(main())