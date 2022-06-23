require('dotenv').config();
const pythonServerConfig = (path = "/exchange", method = "GET", ipAddress = process.env.PYTHON_HOSTNAME || "0.0.0.0", portNumber = process.env.PYTHON_PORT|| 5002) =>{
    const options = {
        hostname: ipAddress,
        port: portNumber,
        path: path,
        method: method
    }
    return options;
}
module.exports = {
    pythonServerConfig
 };