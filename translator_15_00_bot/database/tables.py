import sqlite3


connection = sqlite3.connect("../translator.db")
cursor = connection.cursor()

# создаем таблицу пользователей
cursor.executescript("""
    DROP TABLE IF EXISTS users;
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        chat_id BIGINT NOT NULL UNIQUE
    );
""")
connection.commit()


cursor.executescript("""
    DROP TABLE IF EXISTS translations;
    CREATE TABLE IF NOT EXISTS translations(
        translation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        lang_from TEXT,
        lang_to TEXT,
        original_text TEXT,
        translated_text TEXT,
        user_id INTEGER REFERENCES users(user_id)
    );
""")
connection.commit()

