const puppeteer = require('puppeteer');
const responseValidated = require('./responseValidated');
 
async function requestPage(URL, proxy) {
    let browser, page = null;
    try {   
        browser = await puppeteer.launch({
            headless: false,
            args: [`--proxy-server=${proxy}`]
        });
        page = await browser.newPage();
        await page.setDefaultNavigationTimeout(0); 
        await page.goto(URL);
        const pageContent = await page.content(); // html code
        browser.close();
        if (!responseValidated(pageContent)) {
            return { success: false };
        }
        return { success: true, pageContent }
    } catch (err) {
        browser.close();
        console.error(err.message);
        return { success: false };
    }
}

module.exports = requestPage;