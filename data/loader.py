import config
from googletrans import Translator
from telebot import TeleBot

bot = TeleBot(token=config.BOT_TOKEN)
translator = Translator()
