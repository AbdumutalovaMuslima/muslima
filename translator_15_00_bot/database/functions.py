import sqlite3


connection = sqlite3.connect("translator.db", check_same_thread=False)
cursor = connection.cursor()


def add_user(first_name, chat_id):
    sql = """
        INSERT INTO users(first_name, chat_id) VALUES ( ?, ? )
        ON CONFLICT (chat_id) 
        DO UPDATE SET first_name = ?,
                      chat_id = ?;
    """
    cursor.execute(sql, (first_name, chat_id, first_name, chat_id))
    connection.commit()


def get_user_id(chat_id):
    sql = "SELECT user_id FROM users WHERE chat_id = ?;"
    cursor.execute(sql, (chat_id,))
    user_id = cursor.fetchone()
    return user_id[0]


def add_translation(lang_from, lang_to, original_text, translated_text, chat_id):
    user_id = get_user_id(chat_id)
    sql = "INSERT INTO translations(lang_from, lang_to, original_text, translated_text, user_id) VALUES(?,?,?,?,?);"
    cursor.execute(sql, (lang_from, lang_to, original_text, translated_text, user_id))
    connection.commit()


def get_user_translations(chat_id):
    user_id = get_user_id(chat_id)

    sql = "SELECT lang_from, lang_to, original_text, translated_text FROM translations WHERE user_id = ?;"
    cursor.execute(sql, (user_id,))
    translations = cursor.fetchall()  # [('','','',''),(),()]
    return translations
