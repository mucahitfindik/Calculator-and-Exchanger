const http = require('http');
const sendHttpRequest = (res, options, data) =>{

    let body = [];

    const req = http.request(options, res_ => {
        res_.on('data', d => {
        body.push(d);
        }).on('end', () => {
        body = Buffer.concat(body).toString();
        body = JSON.parse(body);
        return res.status(200).json(body);
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