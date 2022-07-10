import os
from typing import Dict

import telebot
import requests
from bs4 import BeautifulSoup
from botaqan2 import get_url, parse_news


#token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot("5112758318:AAHvkL00paIUlom1e3t5tGqzcf56rQzFN2c")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Hi, this a bot for getting popular news from TengriNews")


@bot.message_handler(commands=['tengrinews'])
def get_title(message):
	k = 1
	x = ''
	titles = ["Choose one of the article and send id of the article"]

	name = 'get_title'
	for i in get_url(name).keys():
		titles.append(f'id={k}. ' + i)
		k += 1
	x = '\n'.join(titles)
	bot.reply_to(message, x)


@bot.message_handler(content_types=['text'])
def get_id_news(message):
	try:
		key = int(message.text)
	except:
		bot.send_message(message.chat.id, "Id it's and integer")

	article, picture = parse_news(key)
	article += '\n' + picture
	bot.send_message(message.chat.id, article)



bot.infinity_polling()



