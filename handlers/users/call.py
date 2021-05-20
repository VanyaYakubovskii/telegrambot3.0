from loader import dp
from keyboards.inline.herou1 import hero
from keyboards.inline.сила import power
from keyboards.inline.ловкость import agility
from keyboards.inline.нейтральные import neutral
from keyboards.inline.интелект import intelligence
from keyboards.inline.простые import easy
from keyboards.inline.items import item
from keyboards.inline.сборные import sbor
from keyboards.inline.Назад8 import nazad
from keyboards.inline.Назад9 import nazad1
from keyboards.inline.Назад10 import nazad2
from keyboards.inline.назад11 import nazad3
from keyboards.inline.разряд1 import rz1
from keyboards.inline.назад13 import nazad4
from keyboards.inline.разряд2 import rz2
from keyboards.inline.назад15 import nazad5
from utils.db_api.db import Database
from keyboards.inline.назад20 import nazad20
@dp.callback_query_handler()
async def test_test(call):
    if call.data == "call":
        await call.message.answer(text= 'выбирите атрибут героя',reply_markup=hero)

    elif call.data == "сила":
        await call.message.answer(text='выбирите героя',reply_markup=power)

    elif call.data == "Axe":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Axe')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "SandKing":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('SandKing')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Mars":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Mars')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Anti-mage":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Anti-mage')
        await call.message.answer(us, reply_markup=nazad1)


    elif call.data == "Drow Ranger":
        await call.message.edit_reply_markup()
        us = Database().hero_inf('Drow Ranger')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Juggernaut":
        await call.message.edit_reply_markup()
        us = Database().hero_inf('Juggernaut')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "ловкость":
        await call.message.answer(text='выбирите героя',reply_markup=agility)

    elif call.data == "нейтральные":
        await call.message.answer(text='выбирите разряд',reply_markup=neutral)

    elif call.data == "интелект":
        await call.message.answer(text='выбирите героя',reply_markup=intelligence)

    elif call.data == "Cristal Maiden":
        await call.message.edit_reply_markup()
        us = Database().hero_inf3('Cristal Maiden')
        await call.message.answer(us, reply_markup=nazad2)

    elif call.data == "Puck":
        await call.message.edit_reply_markup()
        us = Database().hero_inf3('Puck')
        await call.message.answer(us, reply_markup=nazad2)

    elif call.data == "Storm Spirit":
        await call.message.edit_reply_markup()
        us = Database().hero_inf3('Storm Spirit')
        await call.message.answer(us, reply_markup=nazad2)

    elif call.data == "простые":
        await call.message.answer(text='выбирите предмет',reply_markup=easy)

    elif call.data == "Town Portal Scroll":
        await call.message.edit_reply_markup()
        us = Database().item_inf('Town Portal Scroll')
        await call.message.answer(us, reply_markup=nazad3)

    elif call.data == "Ironwood Branch":
        await call.message.edit_reply_markup()
        us = Database().item_inf('Ironwood Branch')
        await call.message.answer(us, reply_markup=nazad3)

    elif call.data == "Quelling Blade":
        await call.message.edit_reply_markup()
        us = Database().item_inf('Quelling Blade')
        await call.message.answer(us, reply_markup=nazad3)

    elif call.data == "Назад1":
        await call.message.answer(text='выбирите предмет',reply_markup=hero)

    elif call.data == "Назад2":
        await call.message.answer(text='выбирите предмет',reply_markup=hero)

    elif call.data == "Назад3":
        await call.message.answer(text='выбирите героя',reply_markup=hero)

    elif call.data == "Назад4":
        await call.message.answer(text='выбирите предмет',reply_markup=item)

    elif call.data == "Назад5":
        await call.message.answer(text='выбирите предмет',reply_markup=item)

    elif call.data == "сборные":
        await call.message.answer(text='выбирите предмет',reply_markup=sbor)

    elif call.data == "Назад6":
        await call.message.answer(text='выбирите предмет',reply_markup=item)

    elif call.data == "Magic Wand":
        await call.message.edit_reply_markup()
        us = Database().item_inf3('Magic Wand')
        await call.message.answer(us, reply_markup=nazad20)


    elif call.data == "Buckler":
        await call.message.edit_reply_markup()
        us = Database().item_inf3('Buckler')
        await call.message.answer(us, reply_markup=nazad20)

    elif call.data == "Veil of Discord":
        await call.message.edit_reply_markup()
        us = Database().item_inf3('Veil of Discord')
        await call.message.answer(us, reply_markup=nazad20)

    elif call.data == "Назад8":
        await call.message.answer(text='выбирите предмет',reply_markup=power)

    elif call.data == "Назад9":
        await call.message.answer(text='выбирите предмет',reply_markup=agility)

    elif call.data == "Назад10":
        await call.message.answer(text='выбирите героя',reply_markup=intelligence)

    elif call.data == "Назад11":
        await call.message.answer(text='выбирите предмет',reply_markup=easy)

    elif call.data == "Разряд 1":
        await call.message.answer(text='выбирите предмет',reply_markup=rz1)

    elif call.data == "Назад12":
        await call.message.answer(text='выбирите предмет',reply_markup=neutral)

    elif call.data == "Keen Optic":
        await call.message.edit_reply_markup()
        us = Database().item_inf2('Keen Optic')
        await call.message.answer(us, reply_markup=nazad4)

    elif call.data == "Ironwood Tree":
        await call.message.edit_reply_markup()
        us = Database().item_inf2('Ironwood Tree')
        await call.message.answer(us, reply_markup=nazad4)

    elif call.data == "Ocean Hert":
        await call.message.edit_reply_markup()
        us = Database().item_inf2('Ocean Hert')
        await call.message.answer(us, reply_markup=nazad4)

    elif call.data == "Назад13":
        await call.message.answer(text='выбирите предмет',reply_markup=rz1)

    elif call.data == "Разряд 2":
        await call.message.answer(text='выбирите предмет',reply_markup=rz2)

    elif call.data == "Назад14":
        await call.message.answer(text='выбирите предмет',reply_markup=neutral)

    elif call.data == "Ring of Aquila":
        await call.message.edit_reply_markup()
        us = Database().item_inf2('Ring of Aquila')
        await call.message.answer(us, reply_markup=nazad5)
    elif call.data == "Imp Claw":
        await call.message.edit_reply_markup()
        us = Database().item_inf2('Imp Claw')
        await call.message.answer(us, reply_markup=nazad5)

    elif call.data == "Nether Shawl":
        await call.message.edit_reply_markup()
        us = Database().item_inf2('Nether Shawl')
        await call.message.answer(us, reply_markup=nazad5)

    elif call.data == "Назад15":
        await call.message.answer(text='выбирите предмет',reply_markup=rz2)

    elif call.data == "Назад20":
        await call.message.answer(text='выбирите предмет',reply_markup=sbor)














