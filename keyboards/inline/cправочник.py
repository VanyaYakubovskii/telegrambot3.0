from aiogram import types



guide = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="мета", callback_data="мета")],
            [types.InlineKeyboardButton(text="роли героев", callback_data="роли героев")],
            [types.InlineKeyboardButton(text="словарь", callback_data="словарь", row_width=1)],
            [types.InlineKeyboardButton(text="советы", callback_data="советы")],
            [types.InlineKeyboardButton(text="моды и команды", callback_data="моды и команды",Fetchrow = 1)],
            [types.InlineKeyboardButton(text="нейтральные крипы", callback_data="нейтральные крипы")],
            [types.InlineKeyboardButton(text="руны", callback_data="руны")],
            [types.InlineKeyboardButton(text="вардинг", callback_data="вардинг")],
            [types.InlineKeyboardButton(text="фарм", callback_data="фарм")

        ]
] )
