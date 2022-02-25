const phpServerConfig = require('../controllers/phpServerConfig')
const httpServer = require('../controllers/httpServer')
const calculation = async (req, res, next) => {
    
    
    if (!req.body.expression){
        res.statusCode = 404;
        res.setHeader('Content-Type', 'application/json');
        return res.json({"error":"Expression Not Found!"});
        //res.status(404).json({Error:"error"});
    }
    const data = JSON.stringify({
        expression : req.body.expression
    });
    const options = phpServerConfig.phpServerConfig(path = req.path, method = req.method);
    options.headers = {
        'Content-Type': 'application/json',
        'Content-Length': data.length
        };
    
    return httpServer.sendHttpRequest(res, options, data);
   /* const statusCode = statusCodeMessage[0];
    const response = statusCodeMessage[1];*/
    

      
};
module.exports = {
   calculation
};