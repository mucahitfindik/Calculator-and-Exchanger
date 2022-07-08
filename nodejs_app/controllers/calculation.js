const phpServerConfig = require('../controllers/phpServerConfig')
const httpServer = require('../controllers/httpServer')
const formula = require("../history/formula")
const historyController  = require('../controllers/history');

const calculation = async (req, res, next) => {
    historyController.search_formula_history(req.body, function(expression_result){
        if(expression_result != null){
            return res.json({result: expression_result});     
        }
        make_exchange_request(req, res, next);
    });  
};
const  make_exchange_request = (req, res, next) =>{
    var data = JSON.stringify(req.body);
    const options = phpServerConfig.phpServerConfig(path = req.path, method = req.method);
    options.headers = {
        'Content-Type': 'application/json',
        'Content-Length': data.length
        };
    httpServer.sendHttpRequest(res, options, data, function(body){
        if(body.error){
            return res.status(400).json(body);
        }
        formula.add_formula_history(req.body.expression, body.result);
        return res.json(body);
    });
}
module.exports = {
   calculation
};