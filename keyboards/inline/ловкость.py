from aiogram import types

agility = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Anti-mage", callback_data="Anti-mage")],
            [types.InlineKeyboardButton(text="Drow Ranger", callback_data="Drow Ranger")],
            [types.InlineKeyboardButton(text="Juggernaut", callback_data="Juggernaut")],
            [types.InlineKeyboardButton(text="<-- Назад", callback_data="Назад2")


        ]
])