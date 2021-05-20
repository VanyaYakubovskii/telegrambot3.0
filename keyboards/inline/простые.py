from aiogram import types

easy = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Town Portal Scroll", callback_data="Town Portal Scroll")],
            [types.InlineKeyboardButton(text="Ironwood Branch", callback_data="Ironwood Branch")],
            [types.InlineKeyboardButton(text="Quelling Blade", callback_data="Quelling Blade")],
            [types.InlineKeyboardButton(text="<-- Назад", callback_data="Назад4")

        ]
])