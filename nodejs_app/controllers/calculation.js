const phpServerConfig = require('../controllers/phpServerConfig')
const httpServer = require('../controllers/httpServer')
const formula = require("../history/formula")
const historyController  = require('../controllers/history');

const calculation = async (req, res, next) => {
    if (!req.body.expression){
        res.statusCode = 404;
        res.setHeader('Content-Type', 'application/json');
        return res.json({"error":"Expression Not Found!"});
        //res.status(404).json({Error:"error"});
    }
    historyController.search_formula_history(req.body, function(expression_result){
        if(expression_result != null){
            return res.json({result: expression_result});
            
        }
        make_exchange_request(req, res, next);
    });  
};
const  make_exchange_request = (req, res, next) =>{
    var data = JSON.stringify({
        expression : req.body.expression
    });
    const options = phpServerConfig.phpServerConfig(path = req.path, method = req.method);
    options.headers = {
        'Content-Type': 'application/json',
        'Content-Length': data.length
        };
    httpServer.sendHttpRequest(res, options, data, function(body,data){
        if(body.result){
            formula.add_formula_history(JSON.parse(data).expression, body.result);
        }
        return res.json(body);
    });
}
module.exports = {
   calculation
};