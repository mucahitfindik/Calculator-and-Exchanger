require('dotenv').config();
const phpServerConfig = (path = "/calculate", method = "GET", ipAddress = process.env.PHP_HOSTNAME || "localhost", portNumber = process.env.PHP_PORT|| 8000) =>{
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