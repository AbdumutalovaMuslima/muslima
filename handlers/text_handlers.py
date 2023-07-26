from telebot import types
from data.loader import bot, translator
from keyboards.default import show_lang_menu
from googletrans import LANGCODES, LANGUAGES
from database.functions import add_translation, get_user_translations


@bot.message_handler(func=lambda msg: msg.text == "Перевод")
def react_to_translation_button(message: types.Message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Выберите язык с которого будем переводить",
                     reply_markup=show_lang_menu())
    bot.register_next_step_handler(message, get_lang_from)


def get_lang_from(message: types.Message):
    chat_id = message.chat.id
    lang_from = LANGCODES[message.text]

    bot.send_message(chat_id, "Выберите язык на который будем переводить",
                     reply_markup=show_lang_menu())
    bot.register_next_step_handler(message, get_lang_to, lang_from)


def get_lang_to(message: types.Message, lang_from: str):
    chat_id = message.chat.id
    lang_to = LANGCODES[message.text]

    bot.send_message(chat_id, "Напишите слово или текст, для перевода",
                     reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, translate, lang_from, lang_to)


def translate(message: types.Message, lang_from: str, lang_to: str):
    chat_id = message.chat.id

    translated_text = translator.translate(message.text, dest=lang_to, src=lang_from).text

    add_translation(lang_from, lang_to, message.text, translated_text, chat_id)
    bot.send_message(chat_id, f"Перевод: {translated_text}")


@bot.message_handler(func=lambda msg: msg.text == "История переводов")
def show_user_translations(message: types.Message):
    chat_id = message.chat.id

    if not get_user_translations(chat_id):
        bot.send_message(chat_id, "Переводов пока что нет")
        return

    bot.send_message(chat_id, "Ваши переводы")
    for lang_from, lang_to, original_text, translated_text in get_user_translations(chat_id):
        bot. send_message(chat_id, f"""
Переведено с: {LANGUAGES[lang_from].title()}
Переведено на: {LANGUAGES[lang_to].title()}
Оригинал: {original_text}
Перевод: {translated_text}
""")