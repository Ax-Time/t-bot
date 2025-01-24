from fastapi import FastAPI, Response, status
import os
from dotenv import load_dotenv
from typing import Optional
import telegram
import telegram.ext
import asyncio

import commands
import commands.start

load_dotenv()
app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

async def main() -> None:
    application = telegram.ext.Application.builder() \
        .token(os.environ.get('TOKEN')) \
        .build()
    
    # Register handlers
    application.add_handler(telegram.ext.CommandHandler('start', commands.start.start))

    # Start the API
    api = FastAPI()

    @api.get('/webhook')
    async def webhook(request):
        await application.update_queue.put(telegram.Update.de_json(data=request.json(), bot=application.bot))
        return Response(status_code=status.HTTP_200_OK)
    
    async with application:
        await application.start()
        await application.stop()

if __name__ == "__main__":
    asyncio.run(main())