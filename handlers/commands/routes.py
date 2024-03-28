from .start import command_start
from aiogram import Router
from typing import Final

commands_router: Final[Router] = Router(name="commands")
commands_router.include_router(command_start)

