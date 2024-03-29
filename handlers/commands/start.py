from keyboards.inline.keyboards import MainMenuBuilder
from aiogram.types import FSInputFile
from aiogram.filters.command import CommandStart
from data.texts import texts
from aiogram import types
from aiogram import Router

command_start = Router(name="start")


@command_start.message(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_photo(
        photo=FSInputFile("data/pics/background.jpg"),
        caption=texts.get("greetings"),
        reply_markup=MainMenuBuilder().get_keyboard()
    )
