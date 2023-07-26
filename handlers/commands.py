from telebot import types

from data.loader import bot
from keyboards.default import show_start_menu
from database.functions import add_user


@bot.message_handler(commands=["start"])
def command_start(message: types.Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    add_user(first_name, chat_id)

    bot.send_message(chat_id, "Привет, я бот переводчик.",
                     reply_markup=show_start_menu(chat_id))
