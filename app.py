from utils.set_bot_commands import set_default_commands
from aiogram import Dispatcher
from loader import dp, bot
import handlers
import asyncio


async def on_startup(dispatcher: Dispatcher):
    await dispatcher.start_polling(bot)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    asyncio.run(on_startup(dp))
