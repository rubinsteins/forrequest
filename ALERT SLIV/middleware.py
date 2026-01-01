import time
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from collections import defaultdict
import loguru
from loguru import logger
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from config import *
from aiogram.types import Message
from loader import *

class RateLimitMiddleware(BaseMiddleware):
    def __init__(self, limit: int, block_time: int, key_prefix: str = 'rate_limit_'):
        self.rate_limit = limit
        self.block_time = block_time
        self.prefix = key_prefix
        self.cache = defaultdict(list)
        self.blocked_users = defaultdict(float)
        super(RateLimitMiddleware, self).__init__()
    async def on_process_message(self, message: types.Message, data: dict):
        user_id = message.from_user.id
        current_time = time.time()

        if user_id in self.blocked_users:
            if current_time < self.blocked_users[user_id]:
                pass
                raise CancelHandler()
            else:
                del self.blocked_users[user_id]
        if user_id in self.cache:
            self.cache[user_id] = [timestamp for timestamp in self.cache[user_id] if current_time - timestamp < self.rate_limit]
            if len(self.cache[user_id]) >= 5:
                await message.answer("<b>🤬Не спамь в бота, пожалуйста! Жди 3 минуты</b>", parse_mode='HTML')
                self.blocked_users[user_id] = current_time + self.block_time
                del self.cache[user_id]
                raise CancelHandler()

        self.cache[user_id].append(current_time)