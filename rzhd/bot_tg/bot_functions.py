import keyboards as kb
import os
import sys
from bot import bot
import db
from utils import RegRequest, RegProject


import process


from datetime import datetime
from aiogram.types import InputMediaPhoto, ParseMode, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.utils.exceptions import MessageNotModified
from aiogram.utils.markdown import text, bold, link


m_text = ''


async def process_start(message):
    try:
        await message.answer(f"Добро пожаловать в телеграм-поисковик \"Оксюморон\"! \n"
                             f"Пожалуйста, выберите опцию, которую Вы хотите найти",
                             reply_markup=kb.menu_kb)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(e, exc_type, file_name, exc_tb.tb_lineno)


async def message_handle(message):
    try:
        if message.text in ["Поиск Проекта по Запросу", "Поиск Запроса по Проекту"]:
            if message.text == "Поиск Проекта по Запросу":
                await RegRequest.year_state.set()
                await message.answer("Укажите год: ", reply_markup=kb.cancel_kb)
            else:
                await RegProject.name_state.set()
                await message.answer("Укажите Название проекта: ", reply_markup=kb.cancel_kb)
        else:
            await message.answer("Извините, я не понимаю")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(e, exc_type, file_name, exc_tb.tb_lineno)


async def request_year_step(message, state, edit=False):
    try:
        msg = message.text
        msg = msg[0].upper() + msg[1:]
        await state.update_data(year=msg)
        await RegRequest.request_theme_state.set()
        await message.answer("Напишите тему запроса:")

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(e, exc_type, file_name, exc_tb.tb_lineno)


async def request_theme_step(message, state, edit=False):
    try:
        msg = message.text
        msg = msg[0].upper() + msg[1:]
        await state.update_data(theme=msg)
        await RegRequest.functional_requester_state.set()
        await message.answer("Укажите функционального заказчика:")

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(e, exc_type, file_name, exc_tb.tb_lineno)


async def functional_requester_step(message, state, edit=False):
    try:
        msg = message.text
        msg = msg[0].upper() + msg[1:]
        await state.update_data(requester=msg)
        user_data = await state.get_data()
        print(str(user_data))

        await bot.send_message(message.from_user.id, "Сейчас найду релевантные проекты")
        # await bot.send_message(message.from_user.id, process.rating_by_words_projects(user_data['theme'].split()),
        #                        reply_markup=kb.menu_kb)
        await bot.send_document(document=open(process.rating_by_words_projects(user_data['theme'])+'.xlsx', 'rb'),
                                chat_id=message.from_user.id,
                                reply_markup=kb.menu_kb)
        await state.finish()

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(e, exc_type, file_name, exc_tb.tb_lineno)


async def cancel_state(message, state):
    try:
        if message.text == "❌ Отмена":
            await message.answer("Действие отменено🗿", reply_markup=kb.menu_kb)
            await state.finish()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(e, exc_type, file_name, exc_tb.tb_lineno)
