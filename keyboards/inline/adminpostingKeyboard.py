from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

adminMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Tasdiqlash", callback_data="confirm"),
    ],
])