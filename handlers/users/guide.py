from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.inline.cправочник import guide
from loader import dp

@dp.message_handler(Command("guide"))
async def show_guide(message: Message):
    await message.answer(text="выберите статью из справочника",
                         reply_markup=guide)