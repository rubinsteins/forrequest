from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *
from data.functions.get_info import *

async def start_kb(user_id):
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text="💎 Start", callback_data="reporter"),
                    InlineKeyboardButton(text="👤 Профиль", callback_data="profil")]
    start_kb.add(*tovarbuttons)
    gengishan = [InlineKeyboardButton(text="📝 Перенос", callback_data="perenesti")]
    start_kb.add(*gengishan)
    helpbutton2 = [InlineKeyboardButton(text="📨 История", callback_data="history")]
    start_kb.add(*helpbutton2)


    if user_id in admin:
        admin_buttons = [
            InlineKeyboardButton(text="⚙️ Админка", callback_data="adminka"),
        ]
        start_kb.add(*admin_buttons)
    return start_kb

async def user_kb():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text="💳 Пополнить", callback_data="popolnit"),
                    InlineKeyboardButton(text="💎 Купить Подписку", callback_data="buysub")]
    start_kb.add(*tovarbuttons)
    gengishan = [InlineKeyboardButton(text="📝 Перенос", callback_data="perenesti"),
                 InlineKeyboardButton(text="🪧 Отключить Рекламу", callback_data="vetements")]
    start_kb.add(*gengishan)
    helpbutton2 = [InlineKeyboardButton(text="📨 История", callback_data="history")]
    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*helpbutton2)
    start_kb.add(*helpbutton23)
    return start_kb

async def bb_kb():
    start_kb = InlineKeyboardMarkup()
    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*helpbutton23)
    return start_kb

async def gomersimpson(user_id):
    price = (await get_price(user_id))[0]
    start_kb = InlineKeyboardMarkup()
    helpbutton232 = [InlineKeyboardButton(text=f"✅ Купить | {price}$", callback_data="buy")]
    start_kb.add(*helpbutton232)
    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*helpbutton23)
    return start_kb

async def buyday_kb():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text=f"💰 Купить", callback_data="daybuy")]
    start_kb.add(*tovarbuttons)

    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*helpbutton23)
    return start_kb

async def buyseven_kb():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text=f"💰 Купить", callback_data="sevenbuy")]
    start_kb.add(*tovarbuttons)

    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*helpbutton23)
    return start_kb

async def buymonth_kb():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text=f"💰 Купить", callback_data="monthbuy")]
    start_kb.add(*tovarbuttons)

    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*helpbutton23)
    return start_kb

async def buyforever_kb():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text=f"💰 Купить", callback_data="foreverbuy")]
    start_kb.add(*tovarbuttons)

    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*helpbutton23)
    return start_kb

async def buysub_kb():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text=f"💰 1 день | 1.5$", callback_data="buyday"),
                    InlineKeyboardButton(text=f"💰 7 дней | 5$", callback_data="buyseven")]
    start_kb.add(*tovarbuttons)
    kup = [InlineKeyboardButton(text=f"💰 Месяц | 10$", callback_data="buymonth"),
           InlineKeyboardButton(text=f"💰 Навсегда | 25$", callback_data="forever")]
    start_kb.add(*kup)
    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*helpbutton23)
    return start_kb

async def backb():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")]
    start_kb.add(*tovarbuttons)
    return start_kb

async def nehvataet_kb():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text="💳 Пополнить", callback_data="popolnit")]
    kup = InlineKeyboardButton(text="💎 Купить Подписку", callback_data="buysub")
    start_kb.add(*tovarbuttons)
    start_kb.add(kup)
    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*helpbutton23)
    return start_kb


async def oplata():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text="💎 CryptoBot", callback_data="cb")]
    kup = InlineKeyboardButton(text="💠 CrystalPay", callback_data="cspay")
    start_kb.add(*tovarbuttons)
    start_kb.add(kup)
    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*helpbutton23)
    return start_kb

def paykb(id: str, url: str, price: float, asset: str):
    kb = InlineKeyboardMarkup(row_width=3)
    kb.insert(InlineKeyboardButton(text='💎 Оплатить', url=url))
    kb.add(InlineKeyboardButton(text='🔄 Проверить', callback_data=f'checkes|{id}|{price}|{asset}'))
    kb.add(InlineKeyboardButton(text='⬅️ Назад', callback_data='cancel'))
    return kb

async def tltprp():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text="🚀 Telethon", callback_data="tlt"),
                    InlineKeyboardButton(text="🔥 Pyrogram", callback_data="prp")]
    start_kb.add(*tovarbuttons)
    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    start_kb.add(*helpbutton23)
    return start_kb

async def tltreport():
    keyboard = InlineKeyboardMarkup()
    q1 = [InlineKeyboardButton("📥 Спам", callback_data="tlt:spam"),
          InlineKeyboardButton("🩸 Насилие", callback_data="tlt:violence")]
    q2 = [InlineKeyboardButton("🚨 ЦП", callback_data="tlt:child_abuse"),
          InlineKeyboardButton("💊 Наркотики", callback_data="tlt:illegal_drugs")]
    q3 = [InlineKeyboardButton("❓ Другое", callback_data="tlt:other"),
          InlineKeyboardButton("🔞 Порнография", callback_data="tlt:pornography")]
    q4 = [InlineKeyboardButton("🗂 Личные данные", callback_data=f"tlt:personal_details")]
    keyboard.add(*q1)
    keyboard.add(*q2)
    keyboard.add(*q3)
    keyboard.add(*q4)
    keyboard.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="back"))
    return keyboard

async def cancelkb():
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")]
    start_kb.add(*tovarbuttons)
    return start_kb

async def bbk():
    start_kb = InlineKeyboardMarkup()
    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="tlt")]
    start_kb.add(*helpbutton23)
    return start_kb

async def bbkprp():
    start_kb = InlineKeyboardMarkup()
    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="prp")]
    start_kb.add(*helpbutton23)
    return start_kb

async def bbkprpof():
    start_kb = InlineKeyboardMarkup()
    helpbutton23 = [InlineKeyboardButton(text="⬅️ Назад", callback_data="profil")]
    start_kb.add(*helpbutton23)
    return start_kb

async def prpreport():
    keyboard = InlineKeyboardMarkup()
    q1 = [InlineKeyboardButton("📥 Спам", callback_data="prp:spam"),
          InlineKeyboardButton("🩸 Насилие", callback_data="prp:violence")]
    q2 = [InlineKeyboardButton("🚨 ЦП", callback_data="prp:child_abuse"),
          InlineKeyboardButton("💊 Наркотики", callback_data="prp:illegal_drugs")]
    q3 = [InlineKeyboardButton("❓ Другое", callback_data="prp:other"),
          InlineKeyboardButton("🔞 Порнография", callback_data="prp:pornography")]
    q4 = [InlineKeyboardButton("🗂 Личные данные", callback_data=f"prp:personal_details")]
    keyboard.add(*q1)
    keyboard.add(*q2)
    keyboard.add(*q3)
    keyboard.add(*q4)
    keyboard.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="back"))
    return keyboard


async def reports_keyboard(user_id, reports, page, total_reports, per_page=5):
    keyboard = InlineKeyboardMarkup(row_width=1)
    for report_id, reason in reports:
        keyboard.add(InlineKeyboardButton(text=f"✅ {reason}", callback_data=f"report_{report_id}"))
    total_pages = (total_reports + per_page - 1) // per_page
    navigation_buttons = []
    if page > 1:
        navigation_buttons.append(InlineKeyboardButton("⬅️ Назад", callback_data=f"history_page_{page - 1}"))
    if page < total_pages:
        navigation_buttons.append(InlineKeyboardButton("Вперёд ➡️", callback_data=f"history_page_{page + 1}"))
    if navigation_buttons:
        keyboard.row(*navigation_buttons)
    keyboard.add(InlineKeyboardButton("⬅️ Назад", callback_data="profil"))

    return keyboard

def crystalpay_kb(id: str, url: str):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.insert(InlineKeyboardButton(text='💸 Оплатить', url=url))
    kb.add(InlineKeyboardButton(text='🔄 Проверить', callback_data=f'checkq_{id}'))
    kb.insert(InlineKeyboardButton(text='⬅️ Назад',  callback_data=f'back'))
    return kb

