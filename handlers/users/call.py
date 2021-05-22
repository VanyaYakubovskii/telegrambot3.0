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
from keyboards.inline.nzspr import nazadspr
from keyboards.inline.cправочник import guide
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

    elif call.data == "Earthshaker":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Earthshaker')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Sven":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Sven')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Tiny":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Tiny')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Kunkka":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Kunkka')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Dragon Knight":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Dragon Knight')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Omniknight":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Omniknight')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Clockwerk":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Clockwerk')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Alchemist":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Alchemist')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Huskar":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Huskar')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Brewmaster":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Brewmaster')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Treant Protector":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Treant Protector')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Centaur Warrunner":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Centaur Warrunner')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Bristleback":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Bristleback')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Timbersaw":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Timbersaw')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Tusk":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Tusk')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Elder Titan":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Elder Titan')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Legion commander":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Legion commander')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Earth Spirit":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Earth Spirit')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Pudge":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Pudge')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Tidehunter":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Tidehunter')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Night Stalker":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Night Stalker')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Phoenix":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Phoenix')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Wraith King":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Wraith King')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Slardar":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Slardar')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Lifestealer":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Lifestealer')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Chaos Knight":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Chaos Knight')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Undying":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Undying')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Spirit Breaker":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Spirit Breaker')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Abaddon":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Abaddon')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Doom":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Doom')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Magnus":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Magnus')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Lycan":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Lycan')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "Underlord":
        await call.message.edit_reply_markup()
        us = Database().hero_inf2('Underlord')
        await call.message.answer(us, reply_markup=nazad)

    elif call.data == "роли героев":
        await call.message.edit_reply_markup()
        us = Database().item_spr('роли героев')
        await call.message.answer(us, reply_markup=nazadspr)

    elif call.data == "Назадспр":
        await call.message.answer(text='выбирите предмет',reply_markup=guide)

    elif call.data == "Vengeful Spirit":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Vengeful Spirit')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Phantom Lancer":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Phantom Lancer')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Morphling":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Morphling')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Riki":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Riki')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Lone Druid":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Lone Druid')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Naga Siren":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Naga Siren')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Ursa":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Ursa')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Templar Assassin":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Templar Assassin')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Ember Spirit":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Ember Spirit')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Bounti Hunter":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Bounti Hunter')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Sniper":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Sniper')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Gyrocopter":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Gyrocopter')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Luna":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Luna')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Troll Warlord":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Troll Warlord')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Faceless Void":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Faceless Void')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Phantom Assassin":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Phantom Assassin')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Razor":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Razor')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Clinkz":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Clinkz')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Shadow Fiend":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Shadow Fiend')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Venomancer":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Venomancer')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Bloodseeker":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Bloodseeker')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Viper":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Viper')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Nyx Assassin":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Nyx Assassin')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Slark":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Slark')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Weaver":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Weaver')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Spectre":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Spectre')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Meepo":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Meepo')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Broodmother":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Broodmother')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Medusa":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Medusa')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Terrorblade":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Terrorblade')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Arc Warden":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Arc Warden')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Monkey King":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Monkey King')
        await call.message.answer(us, reply_markup=nazad1)

    elif call.data == "Pangolier":
        await call.message.edit_reply_markup()
        us =Database().hero_inf('Pangolier')
        await call.message.answer(us, reply_markup=nazad1)

















