from .menu import main_menu_router
from aiogram import Router
from typing import Final

menus_router: Final[Router] = Router(name="menus")
menus_router.include_router(main_menu_router)
