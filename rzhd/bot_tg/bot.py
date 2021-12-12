import aiogram
import config

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

import bot_functions
from utils import RegRequest, RegProject

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

user_ids = [6932]
# 69323263, 497770141


@dp.message_handler(commands="start")
async def process_start_command(message: types.Message):
    if message.from_user.id not in user_ids:
        await bot_functions.process_start(message)
    else:
        await bot.send_message(message.chat.id, 'У вас нет доступа к боту')


@dp.message_handler(content_types=ContentType.TEXT)
async def process_message_handle(message: types.Message):
    if message.from_user.id not in user_ids:
        await bot_functions.message_handle(message)
    else:
        await bot.send_message(message.chat.id, 'У вас нет доступа к боту')


@dp.message_handler(state=[RegRequest.year_state],
                    content_types=ContentType.TEXT)
async def process_request_year_step(message: types.Message, state: FSMContext):
    await bot_functions.cancel_state(message, state)
    current_state = await state.get_state()
    if current_state == "RegRequest:year_state":
        await bot_functions.request_year_step(message, state)


@dp.message_handler(state=[RegRequest.request_theme_state],
                    content_types=ContentType.TEXT)
async def process_short_description_step(message: types.Message, state: FSMContext):
    await bot_functions.cancel_state(message, state)
    current_state = await state.get_state()
    if current_state == "RegRequest:request_theme_state":
        await bot_functions.request_theme_step(message, state)


@dp.message_handler(state=[RegRequest.functional_requester_state],
                    content_types=ContentType.TEXT)
async def process_functional_requester_step(message: types.Message, state: FSMContext):
    await bot_functions.cancel_state(message, state)
    current_state = await state.get_state()
    if current_state == "RegRequest:functional_requester_state":
        await bot_functions.functional_requester_step(message, state)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)