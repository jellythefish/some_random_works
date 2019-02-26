import telebot
from lxml import html
import requests
from telebot.types import Message

#library https://github.com/eternnoir/pyTelegramBotAPI

TOKEN = '764448523:AAH4m7BvpVWHQm8aZ7LoAvuO-uRn4v4gkGo'

bot = telebot.TeleBot(TOKEN)

chat_id = 222599914


@bot.message_handler(regexp="Привет")
def answer_to_hello(message: Message):
    bot.reply_to(message, "Привет, Slava")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    with open('headline.txt') as f:
        lines = f.readlines()
        message = lines[0] + lines[1]
    bot.send_message(chat_id, message)


def send_message(message: Message):
    bot.send_message(chat_id, message)

bot.polling()

