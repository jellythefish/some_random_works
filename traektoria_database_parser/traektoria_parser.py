import requests
from lxml import html
from math import ceil


def our_parsed_page(url):
    response = requests.get(url)
    parsed_page = html.fromstring(response.content)
    return parsed_page


def listofpages(url):
    manypages = bool(parsed_page.xpath('//div[@class="showmemorelabel"]/a/text()'))
    listofpages = []
    if manypages:
        url2 = parsed_page.xpath('//div[@class="showmemorelabel"]/a/@href')
        url_wo_slashes = url.replace('/', '', 2)
        rooturl = url[:url_wo_slashes.index('/') + 2]
        newurl = rooturl + str(url2[0])

        howmanyshow = parsed_page.xpath('//span[@class="howmanyshown_count"]/text()')
        howmanyshow = int(howmanyshow[0])
        allitems = parsed_page.xpath('//div[@class="howmanyshown"]/text()')
        allitems = allitems[0]
        for elem in allitems:
            if not elem.isdigit():
                allitems = allitems.replace(elem, '')
        allitems = int(allitems)
        numberofpages = ceil(allitems / howmanyshow)
        listofpages = [newurl[:-1] + str(x) for x in range(1, numberofpages + 1)]
    else:
        listofpages.append(url)
    return listofpages


url = input("Введите URL: ").strip()
parsed_page = our_parsed_page(url)
database = []

for page in listofpages(url):
    print('.', end='')
    parsed_page = our_parsed_page(page)
    category = parsed_page.xpath('//div[@class="p_info_name"]/span[@itemprop="category"]/text()')
    name = parsed_page.xpath('//div[@class="p_info_name"]/span[@itemprop="name"]/text()')
    price = parsed_page.xpath('//div[@class="price"]/meta[@itemprop="price"]/@content')
    database_of_page = list(zip(category, name, price))
    database.extend(database_of_page)

outfile = open('database.txt', 'w', encoding='utf-8')
for elem in database:
    print(elem[0], elem[1], elem[2], file=outfile)
print('Итого товаров:', len(database), file=outfile)
outfile.close()
print('')
print('OK\nWrited to database.txt')
input("Press Enter to exit")
