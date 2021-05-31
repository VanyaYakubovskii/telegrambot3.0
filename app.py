from aiogram import executor



from loader import dp

from handlers.users.start import bot_start
from handlers.users.help import bot_help
from handlers.users.menu import show_menu
from handlers.users.herou import show_herou
from handlers.users.items import show_items
from handlers.users.guide import show_guide


async def menu(dispatcher):
    # Выполняет команду /menu
    await show_menu(dispatcher)

async def start(dispatcher):
    # Выполняет команду /start
    await bot_start(dispatcher)


async def helping(dispatcher):
    # Выполняет команду /help
    await bot_help(dispatcher)

async def herou(dispatcher):
    # Выполняет команду /herou
    await show_herou(dispatcher)

async def items(dispatcher):
    # Выполняет команду /item
    await show_items(dispatcher)

async def guide(dispatcher):
    # Выполняет команду /guide
    await show_guide(dispatcher)




if __name__ == '__main__':
    executor.start_polling(dp)
