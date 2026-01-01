from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import *
from config import *
from data.functions.get_info import *
from keyboards.user_kb import *
from keyboards.admin_kb import *
from aiogram.dispatcher.filters.state import StatesGroup, State
from states.user_state import *
from states.admin_state import *
from aiogram.types import Message
import aiogram
from datetime import datetime, timedelta

@dp.callback_query_handler(lambda call: call.data == 'adminka')
async def adminish(call: types.CallbackQuery):
    user_id = call.from_user.id

    if user_id in admin:
        await bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=f"⚙️ Админка", reply_markup=await startap(), parse_mode='HTML'
        )
    else:
        for i in admin:
            await bot.send_message(i, f"<b>⚠️ Попытка взлома админ-панели | ID:</b> <code>{user_id}</code>", parse_mode='HTML')

@dp.callback_query_handler(lambda call: call.data == 'give')
async def gevebenee(call: types.CallbackQuery):
    user_id = call.from_user.id

    if user_id in admin:
        await bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption="<b>💎 Введи айди юзера</b>",
            reply_markup=await backb(),
            parse_mode='HTML'
        )
        await givebalance.user.set()
    else:
        for i in admin:
            await bot.send_message(i, f"<b>⚠️ Попытка взлома админ-панели | ID:</b> <code>{user_id}</code>", parse_mode='HTML')

@dp.message_handler(state=givebalance.user)
async def giving(message: types.Message, state: FSMContext):
    try:
        user_id = int(message.text)  
        async with state.proxy() as data:
            data['user_id'] = user_id

        await message.answer("<b>💰 Введи сумму для зачисления</b>", parse_mode='HTML')
        await givebalance.suma.set()
    except ValueError:
        await message.answer("<b>🚫 Ошибка! Введи корректный числовой ID</b>", parse_mode='HTML')

@dp.message_handler(state=givebalance.suma)
async def paygorno(message: types.Message, state: FSMContext):
    try:
        amount = float(message.text)
        async with state.proxy() as data:
            user_id = data['user_id']
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("SELECT balance FROM templates WHERE user_id = ?", (user_id,))
        result = cur.fetchone()
        if result:
            new_balance = result[0] + amount
            cur.execute("UPDATE templates SET balance = ? WHERE user_id = ?", (new_balance, user_id))
            con.commit()
            await message.answer(f"<b>✅ Баланс {user_id} пополнен на {amount} $</b>", parse_mode='HTML')
            await state.finish()
        else:
            await message.answer("<b>❌ Ошибка! Пользователь не найден в бд</b>", parse_mode='HTML')
            await state.finish()
        con.close()
        await state.finish()
    except ValueError:
        await message.answer("<b>🚫 Ошибка! Введи корректное число</b>", parse_mode='HTML')



@dp.callback_query_handler(lambda call: call.data == 'getbalance')
async def gev2342335ebe3522nee(call: types.CallbackQuery):
    user_id = call.from_user.id

    if user_id in admin:
        await bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption="<b>💎 Введи айди юзера для забирания баланса</b>",
            reply_markup=await backb(),
            parse_mode='HTML'
        )
        await getbalance.user.set()
    else:
        for i in admin:
            await bot.send_message(i, f"<b>⚠️ Попытка взлома админ-панели | ID:</b> <code>{user_id}</code>", parse_mode='HTML')

@dp.message_handler(state=getbalance.user)
async def ge333ti333ng(message: types.Message, state: FSMContext):

    try:
        user_id = int(message.text)
        async with state.proxy() as data:
            data['user_id'] = user_id
            balance = (await get_balance(user_id))[0]
        await message.answer(f"<b>⚙️ Баланс юзера: {balance}$\n\n💰 Введи сумму для забирания</b>", parse_mode='HTML')
        await getbalance.suma.set()
    except ValueError:
        await message.answer("<b>🚫 Ошибка! Введи корректный числовой ID</b>", parse_mode='HTML')

@dp.message_handler(state=getbalance.suma)
async def di523ld532o325k(message: types.Message, state: FSMContext):
    try:
        amount2 = float(message.text)
        async with state.proxy() as data:
            user_id = data['user_id']
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("SELECT balance FROM templates WHERE user_id = ?", (user_id,))
        result = cur.fetchone()
        if result:
            current_balance = result[0]
            if current_balance >= amount2:
                new_balance = current_balance - amount2
                cur.execute("UPDATE templates SET balance = ? WHERE user_id = ?", (new_balance, user_id))
                con.commit()
                await message.answer(f"<b>✅ Баланс {user_id} удален на {amount2} $</b>", parse_mode='HTML')
                await state.finish()
            else:
                await message.answer("<b>❌ Ошибка! Недостаточно средств на балансе</b>", parse_mode='HTML')
                await state.finish()
        else:
            await message.answer("<b>❌ Ошибка! Пользователь не найден в БД</b>", parse_mode='HTML')
            await state.finish()
        con.close()
    except ValueError:
        await message.answer("<b>🚫 Ошибка! Введи корректное число</b>", parse_mode='HTML')







@dp.callback_query_handler(lambda call: call.data == 'zabrat')
async def venom(call: types.CallbackQuery):
    user_id = call.from_user.id

    if user_id in admin:
        await bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption="<b>💎 Введи айди юзера для поиска в бд</b>",
            reply_markup=await backb(),
            parse_mode='HTML'
        )
        await getsabaka.user.set()
    else:
        for i in admin:
            await bot.send_message(i, f"<b>⚠️ Попытка взлома админ-панели | ID:</b> <code>{user_id}</code>", parse_mode='HTML')


@dp.message_handler(state=getsabaka.user)
async def ge333ti333ng(message: types.Message, state: FSMContext):
    try:
        user_id = int(message.text)
        async with state.proxy() as data:
            data['user_id'] = user_id
            balance = (await get_balance(user_id))[0]
            issub = (await get_aktiv(user_id))[0]
            rekla = (await get_rekla(user_id))[0]
            subdo = (await get_do(user_id))[0]
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton("❌ Забрать сабку", callback_data=f"borat_{user_id}"))
        keyboard.add(InlineKeyboardButton("🚀 Отменить рекламу", callback_data=f"reklama_{user_id}"))
        keyboard.add(InlineKeyboardButton("🍭 Выдать подписку", callback_data=f"givesub_{user_id}"))
        await message.answer(
            f"<b>💎 Профиль юзера</b> <code>{user_id}</code>\n\n"
            f"<b>💸 Баланс юзера: {balance}$</b>\n"
            f"<b>🔹 Реклама: {rekla}</b>\n"
            f"<b>⏰ До: {subdo}</b>\n"
            f"<b>🛡 Подписка: {issub}</b>",
            parse_mode='HTML',
            reply_markup=keyboard
        )
        await state.finish()
    except ValueError:
        await message.answer("<b>🚫 Ошибка! Введи корректный числовой ID</b>", parse_mode='HTML', reply_markup=await backb())

@dp.callback_query_handler(lambda call: call.data.startswith("borat_"))
async def pereodetiygitler(call: types.CallbackQuery):
    user_id = int(call.data.split("_")[1])
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("UPDATE templates SET issub = ?, subto = ? WHERE user_id = ?", ("Отсутствует", "Подписка отсутствует", user_id))
    con.commit()
    con.close()
    await call.answer("✅ Подписка успешно удалена!")
    await bot.send_message(call.message.chat.id, f"<b>✅ Подписка пользователя {user_id} удалена.</b>", parse_mode="HTML")
    await bot.send_message(user_id, f"<b>❌ Ваша подписка была разжалована администратором</b>", parse_mode="HTML")

@dp.callback_query_handler(lambda call: call.data.startswith("reklama_"))
async def getrekla(call: types.CallbackQuery):
    user_id = int(call.data.split("_")[1])
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("UPDATE templates SET wantsreklama = ? WHERE user_id = ?", ("Отсутствует", user_id))
    con.commit()
    con.close()
    await call.answer("✅ Реклама успешно отменена!")
    await bot.send_message(call.message.chat.id, f"<b>✅ Реклама пользователя {user_id} отменена</b>", parse_mode="HTML")

@dp.callback_query_handler(lambda call: call.data.startswith("givesub_"))
async def ddbydl(call: types.CallbackQuery, state: FSMContext):
    user_id = int(call.data.split("_")[1])
    async with state.proxy() as data:
        data["user_id"] = user_id
    await call.message.answer("<b>⏳ Введите количество дней подписки</b>", parse_mode='HTML')
    await GiveSubState.days.set()

@dp.message_handler(state=GiveSubState.days)
async def geniy(message: types.Message, state: FSMContext):
    try:
        days = int(message.text)
        if days <= 0:
            raise ValueError

        async with state.proxy() as data:
            user_id = data["user_id"]
        end_date = (datetime.now() + timedelta(days=days)).strftime("%d-%m-%Y")
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("UPDATE templates SET issub = ?, subto = ? WHERE user_id = ?", ("Активна", end_date, user_id))
        con.commit()
        con.close()
        await message.answer(f"<b>✅ Подписка выдана пользователю {user_id} до {end_date}</b>", parse_mode="HTML")
        await state.finish()

    except ValueError:
        await message.answer("🚫 Ошибка! Введите корректное количество дней.")








@dp.callback_query_handler(lambda c: c.data.startswith("rasil"))
async def rsilkb(callback_query: types.CallbackQuery):
    await bot.edit_message_caption(
        caption="<b>🌩 Выбери тип рассылки</b>",
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=await reasilkb(),
        parse_mode='HTML'
    )





@dp.callback_query_handler(lambda c: c.data == "withbuton")
async def askhyuikolpext(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "<b>♻️ Введите текст рассылки</b>", parse_mode='HTML', reply_markup=await cancelkb1())
    await BroadcastState.message_text.set()

@dp.message_handler(state=BroadcastState.message_text)
async def askyuiolrr45t(message: types.Message, state: FSMContext):
    await state.update_data(message_text=message.text)
    await message.answer("<b>♻️ Введите текст кнопки</b>", parse_mode='HTML', reply_markup=await cancelkb1())
    await BroadcastState.button_text.set()

@dp.message_handler(state=BroadcastState.button_text)
async def agyhjyujvf(message: types.Message, state: FSMContext):
    await state.update_data(button_text=message.text)
    await message.answer("<b>♻️ Введите ссылку редиректа кнопки рекламы (Указывать строго с https://)</b>", parse_mode='HTML', reply_markup=await cancelkb1())
    await BroadcastState.button_url.set()

@dp.message_handler(state=BroadcastState.button_url)
async def zxcvbnmeerf(message: types.Message, state: FSMContext):
    await state.update_data(button_url=message.text)
    data = await state.get_data()
    await state.finish()

    users = get_users()
    sent_count = 0
    failed_count = 0
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(data['button_text'], url=data['button_url']))

    for user_id in users:
        try:
            await bot.send_message(user_id, data['message_text'], reply_markup=keyboard, parse_mode='HTML')
            sent_count += 1
        except:
            failed_count += 1

    for g in admin:
        report = (f"✅ Рассылка завершена.\n\n"
                  f"📬 Успешно отправлено: {sent_count}\n"
                  f"❌ Не отправлено: {failed_count}")
        await bot.send_message(g, report)


@dp.callback_query_handler(lambda c: c.data == "withphoto")
async def poiuytrewqasdfghjk(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("<b>♻️ Введите текст рассылки</b>", parse_mode='HTML', reply_markup=await cancelkb1())
    await state.set_state(BroadcastStatePhoto.waiting_for_text)

@dp.message_handler(state=BroadcastStatePhoto.waiting_for_text)
async def zswerfghjkl(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("<b>♻️ Введите ссылку на фото рассылки</b>", parse_mode='HTML', reply_markup=await cancelkb1())
    await state.set_state(BroadcastStatePhoto.waiting_for_photo_url)

@dp.message_handler(state=BroadcastStatePhoto.waiting_for_photo_url)
async def rghyuiopjhgfl(message: Message, state: FSMContext):
    data = await state.get_data()
    text = data["text"]
    photo_url = message.text
    users = get_users()
    sent_count = 0
    failed_count = 0
    for user_id in users:
        try:
            await bot.send_photo(chat_id=user_id, photo=photo_url, caption=text, parse_mode='HTML')
            sent_count += 1
        except:
            failed_count += 1
    for j in admin:
        report = f"✅ Рассылка завершена.\n\n📬 Успешно отправлено: {sent_count}\n❌ Не отправлено: {failed_count}"
        await bot.send_message(chat_id=j, text=report)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data == "onlytext")
async def ashyujhuyh(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "<b>♻️ Введите текст рассылки</b>", parse_mode='HTML', reply_markup=await cancelkb1())
    await BroadcastStateText.message_text.set()

@dp.message_handler(state=BroadcastStateText.message_text)
async def szovnat(message: types.Message, state: FSMContext):
    text = message.text
    await state.finish()

    users = get_users()
    sent_count = 0
    failed_count = 0

    for user_id in users:
        try:
            await bot.send_message(user_id, text, parse_mode='HTML')
            sent_count += 1
        except:
            failed_count += 1

    for g in admin:
        report = (f"✅ Рассылка завершена.\n\n"
                  f"📬 Успешно отправлено: {sent_count}\n"
                  f"❌ Не отправлено: {failed_count}")
        await bot.send_message(g, report)


@dp.callback_query_handler(lambda c: c.data == "butonplusfotka")
async def asalamamalik(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "<b>♻️ Введите текст рассылки</b>", parse_mode='HTML',
                           reply_markup=await cancelkb1())
    await foktpaljd.message_text.set()


@dp.message_handler(state=foktpaljd.message_text)
async def asgyuiolkjhgfrtyui(message: types.Message, state: FSMContext):
    await state.update_data(message_text=message.text)
    await bot.send_message(message.from_user.id, "<b>🔗 Введите текст для кнопки</b>", parse_mode='HTML', reply_markup=await cancelkb1())
    await foktpaljd.button_text.set()


@dp.message_handler(state=foktpaljd.button_text)
async def tyuiokjhgfrtyu(message: types.Message, state: FSMContext):
    await state.update_data(button_text=message.text)
    await bot.send_message(message.from_user.id, "<b>🔗 Введите URL для кнопки</b>", parse_mode='HTML', reply_markup=await cancelkb1())
    await foktpaljd.button_url.set()


@dp.message_handler(state=foktpaljd.button_url)
async def gftyuiolkjmnhgf(message: types.Message, state: FSMContext):
    await state.update_data(button_url=message.text)
    await bot.send_message(message.from_user.id, "<b>📷 Введите ссылку на фото для рассылки</b>", parse_mode='HTML', reply_markup=await cancelkb1())
    await foktpaljd.waiting_for_photo_url.set()


@dp.message_handler(state=foktpaljd.waiting_for_photo_url)
async def sfgyuikjhbgf(message: types.Message, state: FSMContext):
    await state.update_data(photo_url=message.text)
    data = await state.get_data()
    text = data['message_text']
    button_text = data['button_text']
    button_url = data['button_url']
    photo_url = data['photo_url']
    users = get_users()
    sent_count = 0
    failed_count = 0
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(button_text, url=button_url))

    for user_id in users:
        try:
            await bot.send_photo(user_id, photo=photo_url, caption=text, reply_markup=keyboard, parse_mode='HTML')
            sent_count += 1
        except Exception as e:
            print(f"Ошибка при отправке пользователю {user_id}: {e}")
            failed_count += 1

    for g in admin:
        report = (f"✅ Рассылка завершена.\n\n"
                  f"📬 Успешно отправлено: {sent_count}\n"
                  f"❌ Не отправлено: {failed_count}")
        await bot.send_message(g, report)

    await state.finish()

@dp.callback_query_handler(lambda call: call.data == "statistica")
async def stata(call: types.CallbackQuery):
    con_users = sqlite3.connect("users.db")
    cur_users = con_users.cursor()
    total_users = cur_users.execute("SELECT COUNT(*) FROM templates").fetchone()[0]
    total_subscriptions = cur_users.execute("SELECT COUNT(*) FROM templates WHERE issub != 'Отсутствует'").fetchone()[0]
    no_ads_users = cur_users.execute("SELECT COUNT(*) FROM templates WHERE wantsreklama != 'Имеется'").fetchone()[0]
    ad_price = cur_users.execute("SELECT pricereklama FROM templates LIMIT 1").fetchone()[0]
    con_users.close()
    con_reports = sqlite3.connect("reports.db")
    cur_reports = con_reports.cursor()
    total_reports = cur_reports.execute("SELECT COUNT(*) FROM templates").fetchone()[0]
    con_reports.close()
    stats_text = f"""
    ⚙️ <b>Статистика</b>

🧑‍💻 <b>Юзеров:</b> <code>{total_users}</code>
💵 <b>Подписки:</b> <code>{total_subscriptions}</code>
🚀 <b>Кол-во репортов:</b> <code>{total_reports}</code>
📦 <b>Без рекламы:</b> <code>{no_ads_users}</code>

💸 <b>Цена на рекламу:</b> <code>{ad_price}$</code>
    """
    await call.message.edit_caption(
        caption=stats_text,
        parse_mode="HTML",
        reply_markup=await bacadmin()
    )

@dp.callback_query_handler(lambda call: call.data == "priceoff")
async def tfyughio(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption="<b>💰 Введите новую сумму для отключения рекламы:</b>",
        parse_mode="HTML",
        reply_markup=await cancelkb()
    )
    await setprice.price.set()


@dp.message_handler(state=setprice.price)
async def prgayce(message: types.Message, state: FSMContext):
    try:
        new_price = float(message.text)
        if new_price <= 0:
            raise ValueError("Цена не может быть отрицательной или равной нулю.")
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("UPDATE templates SET pricereklama = ?", (new_price,))
        con.commit()
        con.close()
        await message.answer(f"<b>✅ Новая цена для отключения рекламы: {new_price} $</b>", parse_mode="HTML")
        await state.finish()

    except ValueError:
        await message.answer("<b>🚫 Ошибка! Введите корректное числовое значение.</b>", parse_mode="HTML")


