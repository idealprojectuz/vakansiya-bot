from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import mainKeyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    with open('jobs.png', 'rb') as file:
        await message.answer_photo(photo=file.read(), caption=f"Assalom alaykum {message.from_user.first_name} Ayti jobs kanalining rasmiy botiga xush kelibsiz! /help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!", reply_markup=mainKeyboard)