from .commands.routes import commands_router
from .users.routes import menus_router
from loader import main_router


main_router.include_router(commands_router)
main_router.include_router(menus_router)
