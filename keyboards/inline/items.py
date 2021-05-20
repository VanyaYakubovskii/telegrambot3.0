from aiogram import types



item = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="простые", callback_data="простые")],
            [types.InlineKeyboardButton(text="сборные", callback_data="сборные")],
            [types.InlineKeyboardButton(text="нейтральные", callback_data="нейтральные")

        ]
])