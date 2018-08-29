import telebot
import buttonsNames
import sqlite3

class RentalOfProperty(telebot.TeleBot):

    def __init__(self,token):
        self.bot = telebot.TeleBot.__init__(self,token=token)


    def checkUser(id,user_id):
       connect = sqlite3.connect('Users')
       cursor = connect.cursor()

       #cursor.execute("SELECT")

       #connect.commit()
       connect.close()
