from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiocryptopay import AioCryptoPay, Networks
from middleware import *

storage = MemoryStorage()

bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
crypto = AioCryptoPay(token=cryptotoken, network=Networks.MAIN_NET)
dp.middleware.setup(LoggingMiddleware())
dp.middleware.setup(RateLimitMiddleware(limit=10, block_time=180))
