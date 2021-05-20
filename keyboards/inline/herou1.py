
from aiogram import types



hero = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="сила", callback_data="сила")],
            [types.InlineKeyboardButton(text="ловкость", callback_data="ловкость")],
            [types.InlineKeyboardButton(text="интелект", callback_data="интелект")

        ]
])