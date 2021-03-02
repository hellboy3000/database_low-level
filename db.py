import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT
)""")

db.commit()


user_log = input('Имя: ')
user_num = input('Пароль: ')
output = input('Для вывода информации введите y/n:' )


sql.execute("SELECT login FROM users WHERE login = '{user_log}'")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES(?, ?)",(user_log, user_num))
    db.commit()

    print('хорошо')
else:
    print("Уже есть")


if output == 'y':
    for val in sql.execute("SELECT * FROM users"):
        print(val)


