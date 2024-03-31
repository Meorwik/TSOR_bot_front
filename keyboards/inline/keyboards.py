from .callbacks import ActionCallback, RateBotCallback
from aiogram.types.web_app_info import WebAppInfo
from .base import InlineBuilder, FacadeKeyboard
from aiogram.types import InlineKeyboardButton
from data.config import config
from typing import Final, List, Dict

CONTACT_ME_URL: Final[str] = "https://t.me/Meorwik"


class MainMenuBuilder(InlineBuilder):
    __name__ = "MainMenuBuilder"

    _ADJUST_SIZES: List[int] = [1]

    _ACTIONS: Final[Dict[str, str]] = {
        "quiz": "🧑‍💻 Начать квиз",
        "review": "📝 Оставить отзыв",
        "rate": "✨ Оценить бота",
        "contact": "📣 Связаться с автором",
    }

    def _init_keyboard(self) -> None:
        menu_buttons: List[InlineKeyboardButton] = [
            InlineKeyboardButton(
                text=self._ACTIONS.get("quiz"), web_app=WebAppInfo(url=config.WEB_APP_URL)
            ),
            InlineKeyboardButton(text=self._ACTIONS.get("review"), url=CONTACT_ME_URL),
            InlineKeyboardButton(
                text=self._ACTIONS.get("rate"),
                callback_data=ActionCallback(menu_level=self.level, action="rate").pack()
            ),
            InlineKeyboardButton(text=self._ACTIONS.get("contact"), url=CONTACT_ME_URL),

        ]
        self.add(*menu_buttons)


class RateBotMenuBuilder(FacadeKeyboard):
    __name__ = "RateBotMenuBuilder"

    _ADJUST_SIZES: List[int] = [5]

    _FACADE = {
        "🌑": RateBotCallback(rate="rate - 1").pack(),
        "🌘": RateBotCallback(rate="rate - 2").pack(),
        "🌗": RateBotCallback(rate="rate - 3").pack(),
        "🌖": RateBotCallback(rate="rate - 4").pack(),
        "🌕": RateBotCallback(rate="rate - 5").pack(),
    }

    def __init__(self):
        super().__init__(level="RateBotMenu")

