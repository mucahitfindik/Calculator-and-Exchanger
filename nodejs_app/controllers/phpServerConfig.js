require('dotenv').config();
const phpServerConfig = (path = "/calculate", method = "GET", ipAddress = process.env.PHP_HOSTNAME || "0.0.0.0", portNumber = process.env.PHP_PORT|| 8000) =>{
    const options = {
        hostname: ipAddress,
        port: portNumber,
        path: path,
        method: method
    }
    return options;
}
module.exports = {
    phpServerConfig
 };