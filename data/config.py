from typing import Union, Final, List
from dataclasses import dataclass
from os import environ


@dataclass
class Config:
    BOT_TOKEN: Final[str] = environ.get("BOT_TOKEN")
    ADMINS: List[Union[str, int]] = environ.get("ADMINS")
    API_URL: Final[str] = environ.get("")
    WEB_APP_URL: Final[str] = environ.get("WEB_APP_URL")


def read_admins(admins_str: str) -> List[Union[str, int]]:
    admin_separator: str = ', '
    admins: List[str] = admins_str.split(admin_separator)
    return admins


config = Config()
config.ADMINS = read_admins(config.ADMINS)
