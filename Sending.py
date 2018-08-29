import threading
import sqlite3
from telebot import types
import buttonsNames


class Sending(threading.Thread):
    def __init__(self, bot):
        threading.Thread.__init__(self)
        self.bot = bot
        self.startMarkup = types.ReplyKeyboardMarkup(True)
        self.startMarkup.row(buttonsNames.refName)
        # bot.send_message(message.chat.id,'Приветствую тебя,{}!'.format(message.from_user.username),reply_markup=startMarkup)

    def run(self):
        while True:
            connect = sqlite3.connect('Messages')
            cursor = connect.cursor()

            cursor.execute("SELECT * FROM messages WHERE flag LIKE 0 ")
            result = cursor.fetchall()
            #print(result)
            if result != []:
                for i in result:
                    if i[2] == '/start':
                        self.bot.send_message(i[0], 'Приветствую тебя,{}!'.format(i[1]), reply_markup=self.startMarkup)
                        cursor.execute("UPDATE messages SET flag=1 WHERE chat_id={}".format(i[0]))
                        connect.commit()
                    if i[2] == buttonsNames.refName:
                        self.bot.send_message(i[0], 'Вот ваша ссылка t.me/RentalOfProperty_bot?start={}'.format(i[0]))
                        cursor.execute("UPDATE messages SET flag=1 WHERE chat_id={}".format(i[0]))
                        connect.commit()

            connect.commit()
            connect.close()
