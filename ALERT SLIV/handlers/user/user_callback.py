
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import *
from config import *
from data.functions.get_info import *
from keyboards.user_kb import *
from aiogram.dispatcher.filters.state import StatesGroup, State
from states.user_state import *
from aiogram.types import Message
import aiogram
from datetime import datetime, timedelta
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ReportRequest
from telethon.tl.types import (
    InputPeerChannel,
    InputReportReasonSpam,
    InputReportReasonViolence,
    InputReportReasonPornography,
    InputReportReasonChildAbuse,
    InputReportReasonIllegalDrugs,
    InputReportReasonPersonalDetails,
    InputReportReasonOther
)
import re
import os
import random
import asyncio
from data.functions.adds import *
import requests
import json

reasons = {
    "spam": InputReportReasonSpam(),
    "violence": InputReportReasonViolence(),
    "pornography": InputReportReasonPornography(),
    "child_abuse": InputReportReasonChildAbuse(),
    "illegal_drugs": InputReportReasonIllegalDrugs(),
    "personal_details": InputReportReasonPersonalDetails(),
    "other": InputReportReasonOther(),
}

@dp.callback_query_handler(lambda call: call.data == 'profil')
async def texteditprofile(call: types.CallbackQuery):
    user_id = call.from_user.id
    balance = (await get_balance(user_id))[0]
    rekla = (await get_rekla(user_id))[0]
    issub = (await get_aktiv(user_id))[0]
    subdo = (await get_do(user_id))[0]
    reports = await get_reports(user_id)

    if issub == 'Отсутствует':
        await call.message.edit_caption(
            caption=f"<b>💎 Ваш профиль</b>\n\n"
                    f"<b>🆔 ID:</b> <code>{user_id}</code>\n"
                    f"<b>💳 Баланс:</b> <code>{balance}$</code>\n"
                    f"<b>💎 Подписка:</b> <code>{issub}</code>\n\n"
                    f"<b>⏰ До:</b> <code>{subdo}</code>\n"
                    f"<b>🚀 Реклама:</b> <code>{rekla}</code>\n\n"
                    f"<b>❌ Ваша подписка - отсутствует</b>",
            parse_mode='HTML',
            reply_markup=await user_kb()
        )
    else:
        await bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=f"<b>💎 Ваш профиль</b>\n\n"
                    f"<b>🆔 ID:</b> <code>{user_id}</code>\n"
                    f"<b>💳 Баланс:</b> <code>{balance}$</code>\n"
                    f"<b>💎 Подписка:</b> <code>{issub}</code>\n\n"
                    f"<b>⏰ До:</b> <code>{subdo}</code>\n"
                    f"<b>🚀 Реклама:</b> <code>{rekla}</code>\n"
                    f"<b>♻️ Кол-во Репортов:</b> <code>{reports}</code>\n\n"
                    f"<b>✅ Используй кнопки ниже для взаимодействия с профилем</b>",
            parse_mode='HTML',
            reply_markup=await user_kb()
        )

@dp.callback_query_handler(lambda call: call.data == 'buysub')
async def kupislona(call: types.CallbackQuery):
    user_id = call.from_user.id
    issub = (await get_aktiv(user_id))[0]
    if issub == 'Отсутствует':
        await call.message.edit_caption(
            caption=f"<b>💎 Покупка подписки, выбери срок</b>",
            parse_mode='HTML',
            reply_markup=await buysub_kb())
    else:
        await call.message.edit_caption(
            caption=f"<b>❌ У тебя уже есть активная подписка</b>",
            parse_mode='HTML',
            reply_markup=await bbkprpof())

@dp.callback_query_handler(lambda call: call.data == 'buyday')
async def kupiday(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption=f"<b>💎 Уверены, что хотите купить подписку на 1 день?</b>",
        parse_mode='HTML',
        reply_markup=await buyday_kb())

@dp.callback_query_handler(lambda call: call.data == 'daybuy')
async def kupi_day(call: types.CallbackQuery):
    user_id = call.from_user.id
    balance = (await get_balance(user_id))[0]

    if balance < 1.5:
        await call.message.edit_caption(
            caption=f"<b>❌ Недостаточно денег на вашем балансе!</b>\n\n<b>💎 Ваш баланс:</b> <code>{balance}$</code>",
            parse_mode='HTML',
            reply_markup=await bb_kb()
        )
    else:
        nb = balance - 1.5
        nsd = (datetime.now() + timedelta(days=1)).strftime("%d-%m-%Y")
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("UPDATE templates SET balance = ?, issub = ?, subto = ? WHERE user_id = ?",
                    (nb, "Активна", nsd, user_id))
        con.commit()
        con.close()
        await call.message.edit_caption(
            caption=f"<b>✅ Подписка успешно куплена!\n\n💎 Ваша подписка активна до:</b> <code>{nsd}</code>",
            parse_mode='HTML',
            reply_markup=await bb_kb())
        await call.bot.send_message(logs_id, f"<b>💎 Пользователь | {user_id} ✅ Приобрел подписку на день ({nsd})</b>", parse_mode='HTML'
        )











@dp.callback_query_handler(lambda call: call.data == 'buyseven')
async def svo(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption=f"<b>💎 Уверены, что хотите купить подписку на 7 дней?</b>",
        parse_mode='HTML',
        reply_markup=await buyseven_kb())

@dp.callback_query_handler(lambda call: call.data == 'sevenbuy')
async def kupi_seven(call: types.CallbackQuery):
    user_id = call.from_user.id
    balance = (await get_balance(user_id))[0]

    if balance < 5:
        await call.message.edit_caption(
            caption=f"<b>❌ Недостаточно денег на вашем балансе!\n\n💎 Ваш баланс:</b> <code>{balance}$</code>",
            parse_mode='HTML',
            reply_markup=await bb_kb()
        )
    else:
        nb = balance - 1.5
        nsd = (datetime.now() + timedelta(days=7)).strftime("%d-%m-%Y")
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("UPDATE templates SET balance = ?, issub = ?, subto = ? WHERE user_id = ?",
                    (nb, "Активна", nsd, user_id))
        con.commit()
        con.close()
        await call.message.edit_caption(
            caption=f"<b>✅ Подписка успешно куплена!\n\n💎 Ваша подписка активна до:</b> <code>{nsd}</code>",
            parse_mode='HTML',
            reply_markup=await bb_kb())
        for log in admin:
            await call.bot.send_message(log, f"<b>💎 Пользователь | {user_id} ✅ Приобрел подписку на неделю ({nsd})</b>", parse_mode='HTML'
        )




@dp.callback_query_handler(lambda call: call.data == 'buymonth')
async def svomonth(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption=f"<b>💎 Уверены, что хотите купить подписку на 31 дней?</b>",
        parse_mode='HTML',
        reply_markup=await buymonth_kb())

@dp.callback_query_handler(lambda call: call.data == 'monthbuy')
async def kupi_month(call: types.CallbackQuery):
    user_id = call.from_user.id
    balance = (await get_balance(user_id))[0]

    if balance < 10:
        await call.message.edit_caption(
            caption=f"<b>❌ Недостаточно денег на вашем балансе!\n\n💎 Ваш баланс:</b> <code>{balance}$</code>",
            parse_mode='HTML',
            reply_markup=await bb_kb()
        )
    else:
        nb = balance - 10
        nsd = (datetime.now() + timedelta(days=31)).strftime("%d-%m-%Y")
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("UPDATE templates SET balance = ?, issub = ?, subto = ? WHERE user_id = ?",
                    (nb, "Активна", nsd, user_id))
        con.commit()
        con.close()
        await call.message.edit_caption(
            caption=f"<b>✅ Подписка успешно куплена!\n\n💎 Ваша подписка активна до:</b> <code>{nsd}</code>",
            parse_mode='HTML',
            reply_markup=await bb_kb())
        for log in admin:
            await call.bot.send_message(log, f"<b>💎 Пользователь | {user_id} ✅ Приобрел подписку на месяц ({nsd})</b>", parse_mode='HTML'
        )









@dp.callback_query_handler(lambda call: call.data == 'forever')
async def ytfghyuiolkjhgyujo(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption=f"<b>💎 Уверены, что хотите купить подписку навсегда?</b>",
        parse_mode='HTML',
        reply_markup=await buyforever_kb())

@dp.callback_query_handler(lambda call: call.data == 'foreverbuy')
async def kughyuiolkmnbghyujk(call: types.CallbackQuery):
    user_id = call.from_user.id
    balance = (await get_balance(user_id))[0]

    if balance < 25:
        await call.message.edit_caption(
            caption=f"<b>❌ Недостаточно денег на вашем балансе!\n\n💎 Ваш баланс:</b> <code>{balance}$</code>",
            parse_mode='HTML',
            reply_markup=await bb_kb()
        )
    else:
        nb = balance - 25
        nsd = (datetime.now() + timedelta(days=10000)).strftime("%d-%m-%Y")
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("UPDATE templates SET balance = ?, issub = ?, subto = ? WHERE user_id = ?",
                    (nb, "Активна", nsd, user_id))
        con.commit()
        con.close()
        await call.message.edit_caption(
            caption=f"<b>✅ Подписка успешно куплена!\n\n💎 Ваша подписка активна до:</b> <code>Навсегда</code>",
            parse_mode='HTML',
            reply_markup=await bb_kb())
        for log in admin:
            await call.bot.send_message(log, f"<b>💎 Пользователь | {user_id} ✅ Приобрел подписку навсегда ({nsd})</b>", parse_mode='HTML'
        )


@dp.callback_query_handler(lambda call: call.data == 'reporter')
async def mamont(call: types.CallbackQuery):
    user_id = call.from_user.id
    issub = (await get_aktiv(user_id))[0]

    if issub == 'Отсутствует':
        await call.message.edit_caption(
            caption=f"<b>❌ Ваша подписка - отсутствует</b>",
            parse_mode='HTML',
            reply_markup=await nehvataet_kb()
        )
    else:
        await call.message.edit_caption(
            caption=f"<b>💎 Выбери модуль репортов</b>",
            parse_mode='HTML',
            reply_markup=await tltprp()  # Здесь не нужно передавать call
        )

@dp.callback_query_handler(lambda call: call.data == 'tlt')
async def tlt(call: types.CallbackQuery):
    user_id = call.from_user.id
    issub = (await get_aktiv(user_id))[0]
    if issub == 'Отсутствует':
        await call.message.edit_caption(
            caption=f"<b>❌ Ваша подписка - отсутствует</b>",
            parse_mode='HTML',
            reply_markup=await nehvataet_kb()
        )
    else:
        await call.message.edit_caption(
            caption=f"<b>💎 Выбери причину репорта</b>",
            parse_mode='HTML',
            reply_markup=await tltreport()
        )

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("tlt"))
async def reasonswat(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    issub = (await get_aktiv(user_id))[0]
    if issub == 'Отсутствует':
        await call.message.edit_caption(
            caption=f"<b>❌ Ваша подписка - отсутствует</b>",
            parse_mode='HTML',
            reply_markup=await nehvataet_kb()
        )
    else:
        reason = callback_query.data.split(":")[1]
        await state.set_state(repomessage.link)
        await state.update_data(reason_str=reason)
        await callback_query.message.edit_caption(
            "<b>🚀 Вы выбрали метод: Telethon\n💎 Введите ссылку на сообщение для репорта</b>",
            reply_markup=await cancelkb(), parse_mode='HTML'
        )

def is_valid_url(url: str) -> bool:
    url_pattern = re.compile(
        r"^(https?://)?" r"(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})" r"(:\d+)?" r"(/[^\s]*)?$"
    )
    return bool(url_pattern.match(url))

@dp.message_handler(state=repomessage.link)
async def misanthropic_division(message: types.Message, state: FSMContext):
    links = message.text.split(",")
    user_id = message.from_user.id
    reason_str = (await state.get_data())["reason_str"]
    if len(links) < 1:
        await state.finish()
        return await message.reply("<b>💎 Введите хотя бы одну ссылку</b>", reply_markup=await cancelkb(), parse_mode='HTML')

    for link in links:
        if not is_valid_url(link):
            await state.finish()
            return await message.reply(f"<b>❌ Ссылка {link} не валидная</b>", reply_markup=await cancelkb(), parse_mode='HTML')

    await state.finish()

    successful_reports = 0
    failed_reports = 0

    for message_link in links:
        if message_link.startswith("https://t.me/c/"):
            parts = message_link.split("/")
            chat_id = int(parts[4])

            try:
                chat = await bot.get_chat(chat_id)
                if chat.type == "private":
                    await message.reply("❌ <b>Чат приватный. Снос невозможен</b>", reply_markup=await cancelkb(), parse_mode='HTML')
                    return
            except Exception:
                await message.reply("❌ <b>Чат приватный. Снос невозможен</b>", reply_markup=await cancelkb(), parse_mode='HTML')
                return
        await bot.send_message(chat_id=user_id, text="<b>🚀 Отправляем репорты...</b>", parse_mode='HTML')
        await state.finish()
        successful, failed = await snos(user_id, message_link, reason_str)
        successful_reports += successful
        failed_reports += failed


    links_str = ' '.join(links)
    response_message = f"<b>💎 Жалобы отправлены</b>\n\n<b>✅ Метод:</b> <code>{reason_str.capitalize()}</code>\n<b>🔗 Ссылка:</b> <code>{links_str}</code>\n\n<b>👤 Репорты успешно отправлены</b>"
    await add_snos(user_id, reason_str, links_str)
    await bot.send_message(chat_id=user_id, text="🚀")
    await bot.send_photo(
        chat_id=user_id,
        photo=photo,
        caption=response_message,
        parse_mode="HTML",
        reply_markup=await bbk()
    )

def filtersnos(message_url):
    path = message_url[len("https://t.me/") :].split("/")
    if len(path) == 2:
        chat_username = path[0]
        message_id = int(path[1])
        return chat_username, message_id
    raise ValueError("Неверная ссылка!")


async def snos(user_id, message_url, reason_str):
    chat_username, message_id = filtersnos(message_url)
    successful_reports = 0
    failed_reports = 0
    successful_sessions = []
    session_files = os.listdir("tltsessions/")
    device_models = ["iPhone 13", "Samsung Galaxy S21", "Google Pixel 6", "OnePlus 9"]
    app_versions = ["8.7.1", "9.3.4", "7.8.9", "8.6.2"]
    async def report_session(session):
        nonlocal successful_reports, failed_reports, successful_sessions

        if not session.endswith(".session"):
            return

        random_api = random.choice(API)
        api_id, api_hash = random_api.split(":")

        device_model = random.choice(device_models)
        app_version = random.choice(app_versions)
        client = TelegramClient(
            f"tltsessions/{session}", api_id, api_hash, auto_reconnect=True,
            device_model=device_model, app_version=app_version
        )

        try:
            await client.connect()

            if not await client.is_user_authorized():
                failed_reports += 1
                await client.disconnect()
                return

            reason = reasons.get(reason_str, InputReportReasonOther())

            await client(ReportRequest(
                peer=chat_username,
                id=[message_id],
                reason=reason,
                message="This user is engaged in telegram spam mailings. Take action",
            ))

            successful_reports += 1
            successful_sessions.append(session)


        except Exception as e:
            pass
            failed_reports += 1
        finally:
            await client.disconnect()

    tasks = []
    for session in session_files:
        if session.endswith(".session"):
            tasks.append(report_session(session))

    try:
        await asyncio.wait_for(asyncio.gather(*tasks), timeout=10)
    except asyncio.TimeoutError:
        await send_report(user_id, message_url, reason_str, successful_reports, failed_reports)
        return successful_reports, failed_reports

    await send_report(user_id, message_url, reason_str, successful_reports, failed_reports)
    return successful_reports, failed_reports


async def send_report(user_id, message_url, reason_str, successful_reports, failed_reports):
    if successful_reports > 0:
        user = await bot.get_chat(user_id)
        user_name = user.username if user.username else " "
        message_text = f"""<b>💎 Новый репорт</b>\n<b>👤 ID:</b> @{user_name} | {user_id}\n<b>🚀 Метод:</b> {reason_str.capitalize()}\n<b>💎 Ссылки:</b> <a href="{message_url}">Перейти</a>
        """

        await bot.send_message(logs_id, message_text, parse_mode="HTML")
    else:
        print("Не удалось отправить жалобу с ни одной сессии.")





@dp.callback_query_handler(lambda call: call.data == 'back')
async def ahmatpidoras(call: types.CallbackQuery):
    user_id = call.from_user.id
    await call.message.edit_caption(
        caption=f'<b>💎 Добро пожаловать в Alert Reporter\n\nℹ️ Используй кнопки ниже для взаимодействия</b>',
        reply_markup=await start_kb(user_id),
        parse_mode='HTML')


@dp.callback_query_handler(lambda call: call.data == "history")
async def show_reports_history(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    page = 1
    reports, total_reports = await get_reports_list(user_id, page)
    if not reports:
        await call.answer("❌ У вас пока нет репортов.")
        return
    keyboard = await reports_keyboard(user_id, reports, page, total_reports)
    await call.message.edit_caption(
        caption="<b>📨 История Репортов\nВыберите репорт для просмотра деталей</b>",
        parse_mode="HTML",
        reply_markup=keyboard
    )


@dp.callback_query_handler(lambda call: call.data.startswith("history_page_"))
async def paginate_reports(call: types.CallbackQuery):
    user_id = call.from_user.id
    page = int(call.data.split("_")[-1])

    reports, total_reports = await get_reports_list(user_id, page)

    keyboard = await reports_keyboard(user_id, reports, page, total_reports)
    await call.message.edit_caption(
        caption="<b>📨 История Репортов</b>\nВыберите репорт для просмотра деталей.",
        parse_mode="HTML",
        reply_markup=keyboard
    )

@dp.callback_query_handler(lambda call: call.data.startswith("report_"))
async def show_report_details(call: types.CallbackQuery):
    report_id = int(call.data.split("_")[-1])

    con = sqlite3.connect("reports.db")
    cur = con.cursor()
    cur.execute("SELECT reason, user FROM templates WHERE id = ?", (report_id,))
    report = cur.fetchone()
    con.close()
    if not report:
        await call.answer("❌ Репорт не найден!")
        return
    reason, user_link = report
    await call.message.edit_caption(
        caption=f"<b>💎 Данные репорта</b>\n\n"
                f"<b>♻️ Метод репорта:</b> <code>{reason}</code>\n"
                f"<b>🚀 Ссылка:</b> <code>{user_link}</code>",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton("⬅️ Назад", callback_data="history")
        )
    )








@dp.callback_query_handler(lambda call: call.data.startswith("popolnit"))
async def ziver(call: types.CallbackQuery):
    user_id = call.from_user.id
    await call.message.edit_caption(
        caption="<b>💳 Выбери способ оплаты</b>",
        parse_mode="HTML",
        reply_markup=await oplata()
    )


@dp.callback_query_handler(lambda call: call.data == 'cb')
async def cryptopaying(call: types.CallbackQuery):
    user_id = call.from_user.id
    await call.message.edit_caption(
        caption="<b>💸 Выбран способ оплаты Cryptobot.\n\nВведите сумму в $ для оплаты (мин - 0.1$)</b>",
        parse_mode='HTML',
        reply_markup=await cancelkb()
    )
    await CryptoBot.money.set()


@dp.message_handler(state=CryptoBot.money)
async def hminsum(message: Message, state: FSMContext):
    try:
        amount_rub = float(message.text)
        if amount_rub < 0.1:
            await message.answer("<b>❌ Минимальная сумма пополнения — 0.10$</b>", parse_mode='HTML')
            return
        amount_usdt = amount_rub
        asset = 'USDT'
        invoice = await crypto.create_invoice(asset=asset, amount=amount_usdt, description='Пополнение баланса')
        kb = paykb(id=invoice.invoice_id, url=invoice.bot_invoice_url, price=amount_usdt, asset=asset)
        await bot.send_message(
            chat_id=message.chat.id,
            text=(
                f"<b>💎 Счет на оплату. Для оплаты нажмите на кнопку Оплатить.</b>"
            ),
            parse_mode='HTML',
            reply_markup=kb
        )
        await state.finish()

    except ValueError:
        await message.answer("<b>❌ Введите нормальное число</b>", parse_mode='HTML')


async def update_user_balancecb(user_id, amount):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("""
        UPDATE templates
        SET balance = balance + ?  
        WHERE user_id = ?
    """, (amount, user_id))
    con.commit()
    con.close()

@dp.callback_query_handler(lambda call: call.data.startswith('checkes'))
async def check(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data.split('|')
    id_pay = data[1]
    amount = float(data[2])
    asset = data[3]
    invoice = await crypto.get_invoices(asset=asset, invoice_ids=int(id_pay))

    try:
        if invoice.status != 'paid':
            await callback.message.edit_text(
                text="<b>❌ Оплата не обнаружена</b>",
                parse_mode='HTML',
                reply_markup=await paybak()
            )
        else:

            await update_user_balancecb(user_id, amount)

            await callback.message.edit_text(
                text=f"<b>💎 Счет успешно оплачен на сумму {amount} USDT методом CryptoBot</b>",
                parse_mode='HTML'
            )
            await bot.send_message(logs_id, f"<b>💎 Юзер {user_id} пополнил баланс на сумму {amount}$ через CryptoBot</b>", parse_mode='HTML')
    except aiogram.utils.exceptions.MessageToEditNotFound:
        await callback.message.answer("❌ Произошла неизвестная ошибка")










@dp.callback_query_handler(lambda call: call.data == 'cspay')
async def balanceuping(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption="<b>💸 Выбран способ оплаты CrystalPay.\n\nВведите сумму в RUB для оплаты (мин - 20 RUB)</b>",
        parse_mode='HTML',
        reply_markup=await cancelkb()
    )
    await UserPay.count.set()

@dp.message_handler(lambda message: not message.text.isdigit() or int(message.text) < 20, state=UserPay.count)
async def check_text(message: types.Message):
    await bot.send_message(message.chat.id, '❌ Минимальная сумма пополнения - 20 рублей')
    return



@dp.message_handler(state=UserPay.count)
async def fsm_pay(message: types.Message, state:FSMContext):
    amount = message.text

    await bot.send_message(message.chat.id, '<b>⌛️ Создаем счет на оплату...</b>', parse_mode='HTML')

    url = 'https://api.crystalpay.io/v2/invoice/create/'
    headers = {'Content-Type': 'application/json'}

    payload = {
        'auth_login': f'{login}',
        'auth_secret': f'{secret}',
        'amount': amount,
        'amount_currency': 'RUB',
        'type': 'purchase',
        'description': 'Пополнение',
        'extra': 'Some additional data',
        'lifetime': 10
    }
    import json
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    json_response = response.json()

    if 'id' not in json_response or 'url' not in json_response:
        await message.answer("❌ Ошибка при создании счета! Попробуйте позже.")
        return

    await message.answer(
        f"<b>💎 Счет на оплату. Для оплаты нажмите на кнопку Оплатить.</b>",
        reply_markup=crystalpay_kb(json_response['id'], json_response['url']),
        parse_mode='HTML'
    )

    await state.finish()

@dp.callback_query_handler(text_startswith='checkq_')
async def chek_pay(callback: types.CallbackQuery):
    order = callback.data.split('|')[0][7:]
    user_id = callback.from_user.id

    await callback.message.edit_text(
        text="<b>💸 Подождите, проверяем оплату...</b>",
        parse_mode='HTML'
    )


    url = 'https://api.crystalpay.io/v2/invoice/info/'
    headers = {'Content-Type': 'application/json'}

    payolad_info = {
        'auth_login': f'{login}',
        'auth_secret': f'{secret}',
        'id': order
    }
    import json
    response = requests.post(url, data=json.dumps(payolad_info), headers=headers)
    json_response = response.json()

    if json_response['state'] == 'payed':
        amount = float(json_response['amount']) / 100
        await update_user_balancecb(user_id, amount)
        await callback.message.edit_text(
            text="<b>💎 Оплата прошла успешно, баланс пополнен!</b>",
            parse_mode='HTML'
        )
        await bot.send_message(logs_id, f"<b>💎 Юзер {user_id} пополнил баланс на сумму {amount}$ через CrystalPay</b>",
                               parse_mode='HTML')

    else:
        await callback.answer('❌ Платеж не найден!', show_alert=True)
        await callback.message.edit_text(
            text="<b>❌ Платеж не найден!</b>",
            parse_mode='HTML'
        )

@dp.callback_query_handler(lambda call: call.data == "cancel", state="*")
async def cancel_action(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("❌ Действие отменено /start")



@dp.callback_query_handler(lambda call: call.data == 'perenesti')
async def capto(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT issub, subto FROM templates WHERE user_id = ? AND issub = 'Активна'", (user_id,))
    result = cur.fetchone()
    con.close()
    if result:
        async with state.proxy() as data:
            data["from_user_id"] = user_id
            data["from_issub"] = result[0]
            data["from_subto"] = result[1]

        await call.message.edit_caption(
            caption="<b>💎 Введи ID пользователя, которому хочешь передать подписку</b>",
            parse_mode="HTML",
            reply_markup=await cancelkb()
        )
        await Usersub.transfer_to.set()
    else:
        await call.message.answer("<b>❌ У вас нет активной подписки для переноса</b>", parse_mode="HTML")

@dp.message_handler(state=Usersub.transfer_to)
async def trnsformerz(message: types.Message, state: FSMContext):
    try:
        to_user_id = int(message.text)
        async with state.proxy() as data:
            from_user_id = data["from_user_id"]
            from_issub = data["from_issub"]
            from_subto = data["from_subto"]

        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("SELECT user_id FROM templates WHERE user_id = ?", (to_user_id,))
        result = cur.fetchone()

        if not result:
            await message.answer("<b>❌ Ошибка! Пользователь не найден в базе данных.</b>", parse_mode="HTML")
            await state.finish()
            return
        cur.execute("UPDATE templates SET issub = ?, subto = ? WHERE user_id = ?", (from_issub, from_subto, to_user_id))
        cur.execute("UPDATE templates SET issub = 'Отсутствует', subto = 'Подписка отсутствует' WHERE user_id = ?", (from_user_id,))
        con.commit()
        con.close()

        await message.answer(f"<b>✅ Подписка успешно передана пользователю {to_user_id}!</b>", parse_mode="HTML")
        await bot.send_message(to_user_id, f"<b>✅ Вам была передана подписка!</b>", parse_mode="HTML")
        await state.finish()
    except ValueError:
        await message.answer("<b>🚫 Ошибка! Введите корректный числовой ID.</b>", parse_mode="HTML")




@dp.callback_query_handler(lambda call: call.data == 'vetements')
async def spemavishycalass(call: types.CallbackQuery):
    user_id = call.from_user.id
    price = (await get_price(user_id))[0]
    await call.message.edit_caption(
        caption=f"<b>✅ Отключение рекламы стоит {price}$\n\n⚡️Уверены, что хотите купить?</b>",
        parse_mode='HTML',
        reply_markup=await gomersimpson(user_id)
    )

@dp.callback_query_handler(lambda call: call.data == 'buy')
async def sowilo(call: types.CallbackQuery):
    user_id = call.from_user.id
    price = (await get_price(user_id))[0]
    balance = (await get_balance(user_id))[0]
    rekla = (await get_rekla(user_id))[0]

    if rekla == "Отсутствует":
        await call.message.answer("<b>❌ Услуга уже куплена!</b>",
                                  parse_mode="HTML")
        return

    if balance >= price:
        new_balance = balance - price
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("UPDATE templates SET balance = ?, wantsreklama = 'Отсутствует' WHERE user_id = ?", (new_balance, user_id))
        con.commit()
        con.close()
        await call.message.answer("<b>✅ Покупка успешна!</b> <code>Реклама отключена</code>", parse_mode="HTML")
    else:
        await call.message.answer("<b>❌ Недостаточно средств!</b> <code>Пополните баланс и попробуйте снова</code>", parse_mode="HTML")



@dp.callback_query_handler(lambda call: call.data == 'inform')
async def inform(call: types.CallbackQuery):
    user_id = call.from_user.id
    await call.message.edit_caption(
        caption=f'<b>💎 Делаем ликвидацию любого аккаунта с помощью ботнета ⚡️\n\nНаши преимущества:\n• Отправка жалоб с 210 аккаунтов менее чем за 3 минуты ✔️\n• Ликвидация аккаунта за пару минут ☄️\n• Приятная администрация, доступные цены 🛍\n\n✅ Работы бота: @BotRepWork</b>',
        reply_markup=await bb_kb(),
        parse_mode='HTML')
