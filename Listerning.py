import threading
import sqlite3
from telebot import types
import buttonsNames
class Listerning(threading.Thread):
    def __init__(self,bot):
        threading.Thread.__init__(self)
        self.bot = bot
    def checkRefs(self,message,chat_id):
        connect = sqlite3.connect('Users')
        cursor = connect.cursor()
        print(chat_id)
        cursor.execute("SELECT * FROM users WHERE chat_id like {}".format(message.chat.id))
        if cursor.fetchone() is None:
            print('Рсаботало None')
            cursor.execute("INSERT INTO users(chat_id,friends,amount) VALUES({},'{}',0)".format(message.chat.id,message.chat.id))
            connect.commit()
            if chat_id != "":
                cursor.execute("SELECT * FROM users WHERE chat_id LIKE {}".format(chat_id))
                user_top = cursor.fetchone()
                if user_top is not None:
                    friend_id = user_top[1]
                    friend_id = friend_id.split()
                    for i in friend_id:
                        if int(i) == message.chat.id:
                            return
                    friend_id.append(message.chat.id)
                    print(friend_id)
                    result = ''
                    for i in friend_id:
                        result+=str(i)
                        result+=' '
                    print('result')
                    print(result)
                    cursor.execute("UPDATE users SET friends='{}',amount={} WHERE chat_id LIKE {}".format(result,(len(friend_id)-1),chat_id))
        connect.commit()
        connect.close()

    def run(self):

        @self.bot.message_handler(commands=['start'])
        def messageStart(message):
            self.checkRefs(message,message.text[7:])



            connect = sqlite3.connect('Messages')
            cursor = connect.cursor()

            cursor.execute("INSERT INTO messages(chat_id ,username ,message ,k , flag ) VALUES ({},'{}','{}',0,0)".format(message.chat.id,message.from_user.username,message.text))

            #print(message.text[7:])
            connect.commit()
            connect.close()

        @self.bot.message_handler(content_types=['text'])
        def messageText(message):
            if message.text == buttonsNames.refName:

                connect = sqlite3.connect('Messages')
                cursor = connect.cursor()

                cursor.execute("INSERT INTO messages(chat_id ,username ,message ,k , flag ) VALUES ({},'{}','{}',0,0)".format(message.chat.id,message.from_user.username,buttonsNames.refName))

                #print(message.text[7:])
                connect.commit()
                connect.close()

        self.bot.polling(none_stop=True, interval=0, timeout=20)
