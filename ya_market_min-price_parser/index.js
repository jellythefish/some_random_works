const { initializeProxyList, parse } = require('./scripts');
const { URL } = require('./config');
const process = require('process');

let proxyList = [];
try {
    proxyList = initializeProxyList();
} catch(e) {
    console.error("Error occured while parsing the proxy list: ", e.stack);
}

parse(URL, proxyList).then(res => {
    console.log(res);
    process.exit();
});
