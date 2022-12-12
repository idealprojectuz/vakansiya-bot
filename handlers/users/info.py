from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

@dp.message_handler(Command("info"), state='*')
async def bot_help(message: types.Message, state: FSMContext):
    text=f"Assalomu alaykum yana bir bor {message.from_user.first_name} \n"
    text+=f"Aloqa uchun malu'motlar +998 97 780 14 00 \n"
    text+=f"Telegram: <a href='https://t.me/k_abdullah'>Abdullah</a>"
    await message.answer(text)