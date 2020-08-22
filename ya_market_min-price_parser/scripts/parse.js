const HTMLParser = require('node-html-parser');
const requestPage = require('./requestPage');
const { PRICES_RANGE_CLASSNAME, OUT_OF_STOCK_CLASSNAME, SINGLE_PRICE_CLASSNAME } = require('../constants/constants');

async function parse(URL, proxyList) {
    let response = null;
    let index = 0;
    do {
        index = Math.round(-0.5 + Math.random() * proxyList.length); // random proxy index from 0 to the last in the array
        response = await requestPage(URL, proxyList[index]);
    } while (!response.success)

    const { pageContent } = response;
    const parsedResponse = HTMLParser.parse(pageContent);

    const goodName = parsedResponse.querySelector('title').text.split(' — ')[0];
    const outOfStock = parsedResponse.querySelector(`.${OUT_OF_STOCK_CLASSNAME}`);
    if (outOfStock) {
        return { name: goodName, url: URL, onStock: outOfStock.text };
    }

    const priceRange = parsedResponse.querySelector(`.${PRICES_RANGE_CLASSNAME}`);
    let minPrice = '';
    if (priceRange) {
        minPrice = priceRange.text.split(' — ')[0];
    } else {
        priceBlock = parsedResponse.querySelector(`.${SINGLE_PRICE_CLASSNAME}`);
        minPrice = priceBlock.querySelectorAll('span')[1].text;
    } 
    return { name: goodName, url: URL, minPrice: minPrice };
}

module.exports = parse;