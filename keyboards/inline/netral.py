from aiogram import types

neutral = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Разряд 1", callback_data="Разряд 1")],
            [types.InlineKeyboardButton(text="Разряд 2", callback_data="Разряд 2")],
            [types.InlineKeyboardButton(text="Разряд 3", callback_data="Разряд 3")],
            [types.InlineKeyboardButton(text="Разряд 4", callback_data="Разряд 4")],
            [types.InlineKeyboardButton(text="Разряд 5", callback_data="Разряд 5")],
            [types.InlineKeyboardButton(text="<-- Назад", callback_data="Назад5")



        ]
])