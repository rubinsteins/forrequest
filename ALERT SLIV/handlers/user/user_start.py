from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import bot, dp
from config import *
from data.functions.get_info import *
from keyboards.user_kb import *
from aiogram.dispatcher.filters.state import StatesGroup, State
from states.user_state import *
from aiogram.types import Message
import aiogram

@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    user_id = message.from_user.id
    user_channel1_status = await bot.get_chat_member(chat_id=channel1_id, user_id=user_id)
    user_channel2_status = await bot.get_chat_member(chat_id=channel2_id, user_id=user_id)
    user_id = message.from_user.id
    if await get_user(user_id) is None:
        await register_user(user_id)
    if user_channel1_status['status'] and user_channel2_status['status'] != 'left':
        await bot.send_photo(
            message.chat.id,
            photo=photo,
            caption=f'<b>💎 Добро пожаловать в Alert\n\nℹ️ Используй кнопки ниже для взаимодействия</b>',
            reply_markup=await start_kb(user_id)
        )
    else:
        button = types.InlineKeyboardButton("⚡️Проверить", callback_data="⚡️Проверить")
        channel = types.InlineKeyboardButton("Alert", url='https://t.me/+qygRooFrSO85Nzgy')
        channel2 = types.InlineKeyboardButton("Alert", url='https://t.me/+qygRooFrSO85Nzgy')
        markup = types.InlineKeyboardMarkup(row_width=1).add(channel, channel2, button)
        await bot.send_message(message.from_user.id,
                               f"<b>⚡️Перед использованием бота, пожалуйста подпишитесь на канал</b>",
                               reply_markup=markup, parse_mode='HTML')


@dp.callback_query_handler(lambda call: call.data == '⚡️Проверить')
async def sub_check(call: types.CallbackQuery):
    user_id = call.from_user.id
    user_channel1_status = await bot.get_chat_member(chat_id=channel1_id, user_id=user_id)
    user_channel2_status = await bot.get_chat_member(chat_id=channel2_id, user_id=user_id)
    if user_channel1_status["status"] != "left" and user_channel2_status["status"] != "left":
        await bot.send_message(user_id,
                               "<b>💎 Спасибо за подписку! Отправь</b> /start <b>для работы с ботом</b>",
                               parse_mode='HTML')
    else:
        button = types.InlineKeyboardButton("⚡️Проверить", callback_data="⚡️Проверить")
        channel1_button = types.InlineKeyboardButton("Alert", url=f'https://t.me/+0rujLUUnBRdhNzQ0')
        channel2_button = types.InlineKeyboardButton("Alert | Новости", url=f'https://t.me/+5tS1WPJPSylmNGUy')
        markup = types.InlineKeyboardMarkup(row_width=1).add(button, channel1_button, channel2_button)
        await bot.send_message(user_id,
                               "<b>❌ Вы не подписались на оба канала! Для работы с ботом подпишитесь на каналы и нажмите Проверить</b>",
                               parse_mode='HTML', reply_markup=markup)