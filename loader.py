from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot, Dispatcher, Router
from data.config import config
from typing import Final


bot: Final[Bot] = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp: Final[Dispatcher] = Dispatcher(storage=MemoryStorage())
main_router: Final[Router] = Router(name="main")
dp.include_router(main_router)
