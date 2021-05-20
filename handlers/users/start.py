from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.inline.test1 import test


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Приветствую тебя, {message.from_user.full_name}!",reply_markup=test )



