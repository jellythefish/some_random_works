import time
import requests
from lxml import html
from Include import bot

class Parser:

    def __init__(self, base_url):
        self.base_url = base_url
        self.last_time = ''

    def get_page(self):
        res = requests.get(self.base_url)
        if res.status_code < 400:
            return res.content

    def get_data(self, htmll):
        html_tree = html.fromstring(htmll)
        headline_link = html_tree.xpath('.//a[@class="main__big__link js-yandex-counter"]')[0].get('href')
        headline = html_tree.xpath('.//span[@class="main__big__title"]')[0].text_content()
        return {headline: headline_link}

    def run(self):
        while True:
            print(';')
            page = self.get_page()
            if page is None:
                continue
            self.get_data(page)
            time.sleep(60)

def get_message(dictionary):
    message = ""
    for item in dictionary.items():
        message += item[0]
        message += ". \n"
        message += item[1]
    return message


my_parser = Parser("https://www.rbc.ru/")
page = my_parser.get_page()
rbc_data = my_parser.get_data(page)
message = get_message(rbc_data)
last_headline = rbc_data.keys()
headline_file = open('headline.txt', 'w')
headline_file.write(message)
headline_file.close()
bot.send_message(message)
while True:
    my_parser = Parser("https://www.rbc.ru/")
    page = my_parser.get_page()
    rbc_data = my_parser.get_data(page)
    now_headline = rbc_data.keys()
    if last_headline != now_headline:
        message = get_message(rbc_data)
        headline_file = open('headline.txt', 'w')
        headline_file.write(message)
        headline_file.close()
        bot.send_message(message)
        last_headline = now_headline
    time.sleep(60)
