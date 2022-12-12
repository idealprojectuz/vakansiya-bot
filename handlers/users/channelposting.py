from aiogram import types
from aiogram.types import Message, CallbackQuery
from loader import dp

@dp.callback_query_handler(text="confirm")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    await call.message.answer("Post kanalga yuborildi")
    await call.bot.forward_message('-1001631068155',call.from_user.id, call.message.message_id)
    await call.answer(cache_time=60)