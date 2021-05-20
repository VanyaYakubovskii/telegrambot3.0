
from aiogram import types



power = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Axe", callback_data="Axe")],
            [types.InlineKeyboardButton(text="SandKing", callback_data="SandKing")],
            [types.InlineKeyboardButton(text="Mars", callback_data="Mars")],
            [types.InlineKeyboardButton(text="<-- Назад", callback_data="Назад1")

        ]
])