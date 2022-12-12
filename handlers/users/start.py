from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainKeyboard import mainKeyboard
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    with open('jobs.png', 'rb') as file:
        await message.answer_photo(photo=file.read(), caption=f"Assalom alaykum {message.from_user.first_name} Ayti jobs kanalining rasmiy botiga xush kelibsiz! /help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!", reply_markup=mainKeyboard)
        await state.finish()