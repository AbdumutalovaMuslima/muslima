from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from googletrans import LANGCODES



def show_start_menu(chat_id=None):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

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