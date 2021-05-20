from aiogram import types

intelligence = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Cristal Maiden", callback_data="Cristal Maiden")],
            [types.InlineKeyboardButton(text="Puck", callback_data="Puck")],
            [ types.InlineKeyboardButton(text="Storm Spirit", callback_data="Storm Spirit")],
            [ types.InlineKeyboardButton(text="<-- Назад", callback_data="Назад3")


        ]
])