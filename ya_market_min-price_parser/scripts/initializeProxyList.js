const fs = require('fs');
const path = require("path");
const { PROXY_FILENAME } = require('../config');

function initializeProxyList() {
    try {  
        const data = fs.readFileSync(path.resolve(__dirname, `../constants/${PROXY_FILENAME}`), 'utf8');
        return data.split('\r\n');   
    } catch(e) {
        throw e;
    }
}

module.exports = initializeProxyList;