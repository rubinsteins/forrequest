from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *


async def start_kb(user_id):
    start_kb = InlineKeyboardMarkup()
    tovarbuttons = [InlineKeyboardButton(text="💎 Start", callback_data="buynum"),
                    InlineKeyboardButton(text="👤 Профиль", callback_data="profil")]
    start_kb.add(*tovarbuttons)
    gengishan = [InlineKeyboardButton(text="📝 Перенос", callback_data="rentnomer"),
                 InlineKeyboardButton(text="ℹ️ Информация", callback_data="inform")]
    start_kb.add(*gengishan)
    helpbutton2 = [InlineKeyboardButton(text="📨 История", callback_data="history")]
    start_kb.add(*helpbutton2)


    if user_id in admin:
        admin_buttons = [
            InlineKeyboardButton(text="⚙️ Админка", callback_data="adminka"),
        ]
        start_kb.add(*admin_buttons)
    return start_kb
