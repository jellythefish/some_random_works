const HTMLParser = require('node-html-parser');
const { FORBIDDEN_TITLE, CAPTCHA_IS_NEEDED_TITLE } = require("../constants/constants");

/* function returns true if parser gets the target page or false 
if yandex detects bot or captcha validation is required */

function responseValidated(pageContent) { 
    const parsedResponse = HTMLParser.parse(pageContent);
    const statusTitle = parsedResponse.querySelector('title').text;
    if (statusTitle === FORBIDDEN_TITLE) {
        console.log("Яндексом был обнаружен парсер.");
        return false;
    } else if (statusTitle === CAPTCHA_IS_NEEDED_TITLE) {
        console.log("Требуется ввод капчи.");
        return false;
    }
    return true;
}

module.exports = responseValidated;