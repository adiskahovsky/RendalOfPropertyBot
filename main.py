import RentalOfProperty
import Listerning
import Sending
from telebot import  types
import buttonsNames
import sqlite3
import  tmp
def main():
   pass



if __name__ =='__main__':
    bot = RentalOfProperty.RentalOfProperty('694382485:AAFK4XueMkQzP-H_XRBF944qIXP2MALVyD0')
    obj_lis = Listerning.Listerning(bot)
    obj_send = Sending.Sending(bot)


    obj_lis.start()
    obj_send.start()