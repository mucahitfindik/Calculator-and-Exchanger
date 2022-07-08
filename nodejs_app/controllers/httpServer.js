const http = require('http');
const sendHttpRequest = (res, options, data, cb) =>{

    let body = [];

    const req = http.request(options, res_ => {
        res_.on('data', d => {
        body.push(d);
        }).on('end', () => {
        body = Buffer.concat(body).toString();
        body = JSON.parse(body);
        cb(body);
        });
    });
    req.write(data);
    req.on('error', e=> {
        return res.status(404).json({"error":e});
    });
    
    req.end();

}
module.exports = {
    sendHttpRequest
 };