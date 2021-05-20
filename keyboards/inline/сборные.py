from aiogram import types

sbor = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Magic Wand", callback_data="Magic Wand")],
            [types.InlineKeyboardButton(text="Buckler", callback_data="Buckler")],
            [types.InlineKeyboardButton(text="Veil of Discord", callback_data="Veil of Discord")],
            [types.InlineKeyboardButton(text="<-- Назад", callback_data="Назад6")

        ]
])