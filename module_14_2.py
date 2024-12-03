import sqlite3

connection = sqlite3.connect('not_telegram_1.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
# Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users")
count = cursor.fetchone()[0]
print(count)
# Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
balance = cursor.fetchone()[0]
print(balance)
# Вывести в консоль средний баланс всех пользователей.
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(avg_balance)
print(balance / count)



connection.commit()
connection.close()