# 5379686390:AAFIiCXzN0uNNIOeRUl5riDTXrzfSA3n3b8

from re import I
import telebot
from telebot import types
from convert import conv

token='5379686390:AAFIiCXzN0uNNIOeRUl5riDTXrzfSA3n3b8'
bot=telebot.TeleBot(token)


global cur 
cur = ''
keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row('USD','RUB')


@bot.message_handler(commands=['start'])
def start_message(message):
   
    bot.send_message(message.chat.id, 'Приветствую, выберите валюту для конвертации', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global cur
    global cur2
    
    if message.text.lower() == 'usd':
        cur =''
        cur2 =''
        bot.send_message(message.chat.id, 'Введите сумму для конвертации, например 1000')
        cur = 'usd'
        cur2 = 'rub'
        
    elif message.text.lower() == 'rub':
        cur =''
        cur2 =''
        bot.send_message(message.chat.id, 'Введите сумму для конвертации, например 1000')
        cur ='rub'
        cur2 = 'usd'
    else: 
        amount = message.text.lower()
        x =str(amount)
        if x.isdigit():
            if cur == 'rub' or cur == 'usd':
                result = f'{amount} {cur} -> {conv(cur,cur2, x)}  {cur2}'
                bot.send_message(message.chat.id, result)
                bot.send_message(message.chat.id, "Для продолжения введите /start")
        else :
            bot.send_message(message.chat.id, 'это не число')

bot.polling()