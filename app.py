from aiogram import Dispatcher
from loader import dp, bot
import handlers
import asyncio
import utils


async def on_startup(dispatcher: Dispatcher):
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(on_startup(dp))
