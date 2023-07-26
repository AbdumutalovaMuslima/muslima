# pytelegrambotapi, python-dotenv

from data.loader import bot
import handlers


# TODO: добавить базу данных
# TODO: создать таблицу "users" и "translations"

# TODO: добавить функции для проверки пользователя, добавления пользователя в БД
# TODO: добавить функции для сохранения перевода, для получения переводов определенного пользователя
# TODO: добавить функцию для удаления перевода



if __name__ == '__main__':
    print("БОТ ЗАПУЩЕН")
    bot.infinity_polling()
