# -*- coding: utf-8 -*-
import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import commands, callbacks, states

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_router(commands.router)
dp.include_router(callbacks.router)
dp.include_router(states.router)

async def main():
     await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
