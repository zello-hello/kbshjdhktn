from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.row(
    KeyboardButton("Поиск Проекта по Запросу")
).row(
    KeyboardButton("Поиск Запроса по Проекту")
)

cancel_kb = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_kb.row(
    KeyboardButton("❌ Отмена")
)
