from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.inline.items import item
from loader import dp

@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="выберите вид предмтов",
                         reply_markup=item)
