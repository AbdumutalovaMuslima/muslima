from telebot import TeleBot
from googletrans import Translator
import config

bot = TeleBot(token=config.BOT_TOKEN)
translator = Translator()
