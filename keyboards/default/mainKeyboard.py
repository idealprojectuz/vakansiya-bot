from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sherik Kerak"),
            KeyboardButton(text="ish joy kerak"),
        ],
        [
            KeyboardButton(text="Hodim Kerak"),
            KeyboardButton(text="Ustoz kerak"),
        ],
        [
            KeyboardButton(text="Shogird Kerak"),
        ],
    ],
    resize_keyboard=True
)