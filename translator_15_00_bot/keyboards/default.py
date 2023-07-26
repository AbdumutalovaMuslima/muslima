from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from googletrans import LANGCODES

# en -> English
# uz -> Uzbek
# ru -> Russian


def show_start_menu(chat_id=None):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    # TODO: добавить кнопку "Регистрация" если пользователя нет в базе данных

    kb.row(
        KeyboardButton(text="Перевод"),
        KeyboardButton(text="История переводов")
    )
    return kb


def show_lang_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(lang) for lang in LANGCODES.keys()]
    kb.add(*buttons)
    return kb
