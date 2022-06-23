const pythonServerConfig = require('../controllers/pythonServerConfig')
const httpServer = require('../controllers/httpServer')
const exchange = async (req, res, next) => {
    
    const options = pythonServerConfig.pythonServerConfig(path = req.path, method = req.method);
    options.headers = {
        'Content-Type': 'application/json',
        };
    const data = JSON.stringify({
        expression : req.body.expression
    });
    
    return httpServer.sendHttpRequest(res, options, data);
   /* const statusCode = statusCodeMessage[0];
    const response = statusCodeMessage[1];*/
    

      
};
module.exports = {
   exchange
};