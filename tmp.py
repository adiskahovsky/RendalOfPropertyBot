import sqlite3


connect = sqlite3.connect('Users')
cursor = connect.cursor()
#cursor.execute("DROP TABLE users")
#connect.commit()
#cursor.execute("CREATE TABLE users(chat_id INTEGER, friends TEXT,amount INTEGER)")
#cursor.execute("CREATE TABLE messages(chat_id INTEGER,username TEXT,message TEXT,k INTEGER, flag INTEGER) ")
#cursor.execute("SELECT * FROM messages")
#print(cursor.fetchall())

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())


connect.commit()
connect.close()