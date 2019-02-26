import requests
from pprint import pprint
import telebot


token = "764448523:AAH4m7BvpVWHQm8aZ7LoAvuO-uRn4v4gkGo"


def request_through_proxy(url):
    proxies = {
        'http': 'http://209.97.177.138:8080'
    }
    response = requests.get(url, proxies=proxies)
    return response


def GetMe():
    url = f'https://api.telegram.org/bot{token}/'
    response = requests.get(f'{url}GetMe')
    return response.json()


def GetUpdates():
    url = f'https://api.telegram.org/bot{token}/'
    response = requests.get(f'{url}GetUpdates')
    return response.json()


def sendMessage(chat_id, text):
    url = f'https://api.telegram.org/bot{token}/'
    data = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(f'{url}sendMessage', data=data)
    return response.json()

# pprint(sendMessage(222599914, "Как дела!"))
pprint(GetUpdates())
