from keyboards.inline.keyboards import MainMenuBuilder, RateBotMenuBuilder
from keyboards.inline.callbacks import ActionCallback, BackCallback
from aiogram.types import CallbackQuery
from data.texts import texts
from aiogram import Router
from typing import Final
from aiogram import F


main_menu_router: Final[Router] = Router(name='main_menu')


@main_menu_router.callback_query(ActionCallback.filter(F.menu_level == MainMenuBuilder.get_menu_level()))
async def handle_main_menu(call: CallbackQuery):
    callback = ActionCallback.unpack(call.data)

    if callback.action == "rate":
        await call.message.edit_caption(
            caption=texts.get("rate_bot"),
            reply_markup=RateBotMenuBuilder().get_keyboard()
        )


@main_menu_router.callback_query(BackCallback.filter(F.go_to == MainMenuBuilder.get_menu_level()))
async def handle_back_button(call: CallbackQuery):
    await call.message.edit_caption(
        caption=texts.get("greetings"),
        reply_markup=MainMenuBuilder().get_keyboard()
    )
