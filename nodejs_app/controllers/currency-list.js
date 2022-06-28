const pythonServerConfig = require('../controllers/pythonServerConfig')
const httpServer = require('../controllers/httpServer')
const currency_list = async (req, res, next) => {
    

    const options = pythonServerConfig.pythonServerConfig(path = req.path, method = req.method);
    options.headers = {
        'Content-Type': 'application/json',
        };
    const data = "";
    httpServer.sendHttpRequest(res, options, data, function(body,){
        return res.json(body);
    });
}
module.exports = {
    currency_list
 };