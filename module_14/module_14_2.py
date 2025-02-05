import sqlite3

connection = sqlite3.connect('not_telegram2.db')
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

for i in range(1,11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i}0", "1000"))

for i in range(1,11,2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

for i in range (1,11,3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))

cursor.execute("DELETE FROM Users WHERE username = ?", (f"User6",))

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone () [0]


cursor.execute("SELECT SUM(balance) FROM Users")
all_balances= cursor.fetchone()[0]
print(f"Ответ, используя деление: {all_balances/total_users}")

cursor.execute("SELECT AVG(balance) FROM Users")
second_result = cursor.fetchone()[0]
print(f"Ответ, используя AVG: {second_result}")

connection.commit()
connection.close()