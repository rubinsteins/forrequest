from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *


async def startap():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text="💎 | Выдать", callback_data="give"),
                    InlineKeyboardButton(text="💎 | Забрать", callback_data="getbalance")]
    start_kb.add(*tovarbuttons)
    gengishan = [InlineKeyboardButton(text="💎 | Рассылка", callback_data="rasilka"),
                 InlineKeyboardButton(text="💎 | Поиск юзера", callback_data="zabrat")]
    start_kb.add(*gengishan)
    tovarbuttons2 = [InlineKeyboardButton(text="🎲 | Статистика", callback_data="statistica"),
                     InlineKeyboardButton(text="🎲 | Цена рекламы", callback_data="priceoff")]
    start_kb.add(*tovarbuttons2)
    gengishan2 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*gengishan2)
    return start_kb


async def backb():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")]
    start_kb.add(*tovarbuttons)
    return start_kb

async def bacadmin():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text="⬅️ Назад", callback_data="adminka")]
    start_kb.add(*tovarbuttons)
    return start_kb

async def reasilkb():
    start_kb = InlineKeyboardMarkup()
    helpbutton2 = [InlineKeyboardButton(text="♻️ С кнопкой", callback_data="withbuton"),
                   InlineKeyboardButton(text="♻️ С фоткой", callback_data="withphoto")]
    start_kb.add(*helpbutton2)
    helpbutton232 = [InlineKeyboardButton(text="♻️ Только Текст", callback_data="onlytext")]
    start_kb.add(*helpbutton232)
    helpbutton23 = [InlineKeyboardButton(text="♻️ Фотка + кнопка", callback_data="butonplusfotka")]
    start_kb.add(*helpbutton23)
    ghjk = [InlineKeyboardButton(text="⬅️ Назад", callback_data="adminka")]
    start_kb.add(*ghjk)
    return start_kb

async def cancelkb1():
    start_kb = InlineKeyboardMarkup()
    helpbutton2 = [InlineKeyboardButton(text="❌ Отменить", callback_data="cancel")]
    start_kb.add(*helpbutton2)
    return start_kb





