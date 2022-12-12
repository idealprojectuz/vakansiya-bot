from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Vakansiya qo'shish"),
        ],
    ],
    resize_keyboard=True
)