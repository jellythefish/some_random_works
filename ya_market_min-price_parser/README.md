# Парсер Яндекс Маркета

Приложение, отражающее минимальную цену товара на Я.Маркете.

*Work in progress...*

(Beta):

## Установка

1. Клонируйте репозиторий на свой компюьтер и перейдите в папку с парсером:

```bash
git clone https://github.com/jellythefish/some_random_works/
cd ya_market_min-price_parser
```

	2. Установите зависимости

```bash
npm i
```

## Запуск и тестирование

1. В config.js в поле URL нужно указать ссылку на конкретный товар на Я.Маркете:

```javascript
const PROXY_FILENAME = 'proxy-list.txt';
// ######################## URL RIGHT HERE 
const URL = 'https://market.yandex.ru/product--ochki-virtualnoi-realnosti-dlia-smartfona-samsung-gear-vr-sm-r322/14177537?lr=213&onstock=1';
// ########################

module.exports = { PROXY_FILENAME, URL };
```

2. Для запуска парсера наберите в консоли

```bash
npm run start
```



Чтобы протестировать парсер, наберите в консоли

```bash
npm run test
```

Парсер пройдет по нескольким товарам разных категорий: одно предложение, одна цена, товара нет в наличии, много предложений.

## ToDo

+ Интегрировать с телеграм ботом
+ Интегрировать апи на рандомный прокси

