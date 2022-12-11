from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.login_url import LoginUrl

registration_menu=InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Tizimga kirish", login_url=LoginUrl('https://xakaton.idealproject.uz/')),
    ]
])
