
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.inline.button1 import choice
from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer(text="Меню информации",
                         reply_markup=choice)

