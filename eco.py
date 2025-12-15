import telebot
import os
import random
import requests
import time
from telebot.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
bot = telebot.TeleBot("8540625820:AAGtdRIt-vWYAmVMJGLuoa1WQI0SIQ9am2c")
mems = os.listdir('images1')

@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я эко-бот! Используй команду /eco чтобы узнать об эко-активистах и о том, чем они занимаются!')

@bot.message_handler(commands=['eco'])
def send_eco(message):
    bot.reply_to(message, f'Кто такие эко-активисты?')
    time.sleep(2)
    bot.reply_to(message, f'Эко-активисты - это люди, для которых защита окружающей среды является долгом. Это могут быть профессиональные биологи, студенты, пенсионеры, волонтёры или просто неравнодушные жители.')
    with open(f'images1/image1.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    time.sleep(10)
    bot.reply_to(message, f'Цель экоактивизма — усилить меры по охране природы от загрязнений человеком, предотвратить разрушение среды обитания.')
    with open(f'images1/image2.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    time.sleep(10)
    bot.reply_to(message, f'В мире существует множество эко организаций, таких как WWF, Greenpeace и ВООП.')
    with open(f'images1/image3.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    time.sleep(10)
    bot.reply_to(message, f'Это была маленькая сводка об эко-активистах! Надеюсь, тебе понравилось, и ты сам захочешь стать одним! :)')
    
@bot.message_handler(commands=['plasticrecycle'])
def send_plastic(message):
    bot.reply_to(message, f'Зачем перерабатывать пластик и другой мусор?')
    time.sleep(2)
    bot.reply_to(message, f'Начнём с понятия переработки. Переработка - это процесс, при котором отходы превращаются в новые материалы и изделия.')
    with open(f'images1/image4.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    time.sleep(10)
    bot.reply_to(message, f'Сдавая мусор на переработку, его обрабатывают и превращают в изначальный материал, из которого позже создают новый продукт.')
    with open(f'images1/image5.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    time.sleep(10)
    bot.reply_to(message, f'Если мы будем перерабатывать мусор, то его станет меньше, а различных продуктов - больше!')
    with open(f'images1/image6.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    time.sleep(10)
    bot.reply_to(message, "Это была маленькая статья о переработке, которая помогла лучше понять этот термин и понять, зачем этим заниматься! Спасибо, что прочитали! :)")

bot.infinity_polling()



