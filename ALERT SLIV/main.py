from aiogram import executor
import time
from loader import *
from config import *
from data import database
import loguru
from loguru import logger as log
from handlers.user.user_start import *
from handlers.user.user_callback import *
from handlers.admin.admin_callback import *
import telethon
from utils.pyro import *
from middleware import *
from datetime import datetime
import aiocron


async def startup_bot(dispatcher):
    me = await bot.get_me()
    await bot.send_message(admin[0], f'<b>✅ Бот запущен @{me.username}</b>')
    log.info("bot started")
    log.info(f"bot {me.username} started")

async def backup_data(self):
    log.info("bot off")


async def check_subscriptions():
    today = datetime.now()
    expired_count = 0
    active_subs = 0
    no_ads_users = 0
    con = sqlite3.connect("users.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT user_id, subto FROM templates WHERE subto != 'Подписка отсутствует'")
    users = cur.fetchall()

    for user in users:
        user_id = user['user_id']
        subto = user['subto']

        try:
            subto_date = datetime.strptime(subto, "%d-%m-%Y")
        except ValueError:
            pass
            continue
        if subto_date.date() == today.date():
            cur.execute("""
                UPDATE templates SET subto = 'Подписка отсутствует', issub = 'Отсутствует' WHERE user_id = ?
            """, (user_id,))
            expired_count += 1
            log.info(f"Обновлена подписка для user_id {user_id}")
    cur.execute("SELECT COUNT(*) FROM templates WHERE subto != 'Подписка отсутствует'")
    active_subs = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM templates WHERE wantsreklama != 'Имеется'")
    no_ads_users = cur.fetchone()[0]
    total_users = cur.execute("SELECT COUNT(*) FROM templates").fetchone()[0]
    con.commit()
    con.close()
    report = (f"<b>⚙️ Дамп данных (60 минут)\n"
              f"├ 💎 Юзеры: {total_users}\n"
              f"├ 💎 Подписки: {active_subs}\n"
              f"├ 💎 Без Рекламы: {no_ads_users}\n"
              f"└ 💎 Закончились: {expired_count}</b>")
    await bot.send_message(logs_id, report, parse_mode='HTML')
aiocron.crontab('0 * * * *', func=check_subscriptions)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=startup_bot, on_shutdown=backup_data, skip_updates=True)