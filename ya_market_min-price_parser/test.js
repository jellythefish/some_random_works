const { initializeProxyList, parse } = require('./scripts');

const URLs = {
    ONE_PRICE: [
        'https://market.yandex.ru/product--ochki-virtualnoi-realnosti-dlia-smartfona-samsung-gear-vr-sm-r322/14177537?lr=213&onstock=1',
        'https://market.yandex.ru/offer/fdA6xyNtyVp4KB0Ox0lNyA?cpc=akIFq--uFslA6rKrXJqBCD1hn6whM0mVZOX8ey6fkhuxUjWjF_am3CYTpU0AtaPc5p54hgNrNlQ_q6WG7AMt9MlTPYI21q8VAUbC93bPFFWDOTisO96lvkh41d6tT4gpnib5Ared1rLk4VsdLyou-kiJmWw7Sn-J&from=premiumOffers&lr=213'
    ],
    SINGLE_OFFER: [
        'https://market.yandex.ru/product--wi-fi-router-tp-link-archer-ax50/666930009?nid=55410&show-uid=15980959914621087582716037&context=search&glfilter=4863258%3A14335072&glfilter=4863262%3A100~&onstock=1&lr=213',
        'https://market.yandex.ru/product--wi-fi-router-zyxel-keenetic-air/1715179903?nid=55410&show-uid=15980959914621087582716048&context=search&glfilter=4863258%3A14335072&glfilter=4863262%3A100~&onstock=1&lr=213'
    ],
    MANY_ITEMS: [
        'https://market.yandex.ru/product--nastennaia-split-sistema-aux-asw-h09b4-lk-700r1/1973854888?nid=54976&show-uid=15980955500191913311116002&context=search&glfilter=17269280%3A17271677&onstock=1&lr=213',
        'https://market.yandex.ru/product--udalitel-sorniakov-fiskars-xact-1020126/660759031?show-uid=15980955788670265797316003',
        'https://market.yandex.ru/product--bassein-intex-metal-frame-28200-56997/13735834?nid=59719&show-uid=15980955973214948235716001&context=search&onstock=1&lr=213'
    ],
    OUT_OF_ORDER: [
        'https://market.yandex.ru/product--klaviatura-logitech-g-g105-gaming-keyboard-made-for-call-of-duty-black-usb/7772664?nid=68334&show-uid=15980956341789577421816003&context=search&lr=213&text=G105',
        'https://market.yandex.ru/product--ushm-verto-52g105-500-vt-115-mm/10405657?nid=71674&show-uid=15980956341789577421816005&context=search&lr=213&text=G105',
        'https://market.yandex.ru/product--televizor-lg-105uc9v-105-2014/11136303?nid=59601&show-uid=15980956341789577421816007&context=search&lr=213&text=G105',
        'https://market.yandex.ru/product--bas-gitara-ibanez-g105/10961545?nid=55286&show-uid=15980956341789577421816008&context=search&lr=213&text=G105',
    ]
}


let proxyList = [];
try {
    proxyList = initializeProxyList();
} catch(e) {
    console.error("Error occured while parsing the proxy list: ", e.stack);
}

async function test() {
    const results = [];
    for (let type in URLs) {
        for (let URL of URLs[type]) {
            await parse(URL, proxyList)
                .then(res => results.push({ category: type, ...res }))
        }
    }
    console.log(results);
}

test();