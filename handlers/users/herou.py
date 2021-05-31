from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.inline.herou1 import hero
from loader import dp

@dp.message_handler(Command("herou"))
async def show_herou(message: Message):
    await message.answer(text="выберите основной атрибут героя",
                         reply_markup=hero)



