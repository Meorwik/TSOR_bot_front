from aiogram.filters.command import CommandStart
from aiogram import types
from aiogram import Router

command_start = Router(name="start")


@command_start.message(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
