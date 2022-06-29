const pythonServerConfig = require('../controllers/pythonServerConfig')
const httpServer = require('../controllers/httpServer')
const exchangeStorage = require("../history/exchange-storage")
const historyController  = require('../controllers/history');
const exchange = async (req, res, next) => {
    if (!req.body.amount || !req.body.toCurrency || !req.body.fromCurrency || !req.body.date ){
        res.statusCode = 404;
        res.setHeader('Content-Type', 'application/json');
        return res.json({"error":"Request As Not Expected!"});
    }
    historyController.search_history_exchange_by_date(req.body, function(cross_rates_from_history){
        if(cross_rates_from_history.length == 0){
            return make_exchange_request(req, res, []);
        }
        history_to_currency_list = [];
        history_responses =[];
        cross_rates_from_history.forEach(history => {
            h_response = {
                cross_rate: history.cross_rate,
                result: req.body.amount*history.cross_rate,
                to_currency: history.to_currency,
            }
            history_responses.push(h_response);
            history_to_currency_list.push(history.to_currency);
        });
        req.body.toCurrency= req.body.toCurrency.filter(function(val){
            return history_to_currency_list.indexOf(val) == -1;
        });
        if(req.body.toCurrency.length == 0){
            return res.json(history_responses);
        }
        else{
            return make_exchange_request(req, res, history_responses)
        }  
    });
    
};
const make_exchange_request = (req, res ,cross_rates_from_history) =>{
    const data = JSON.stringify({
        amount : req.body.amount,
        toCurrency : req.body.toCurrency,
        fromCurrency : req.body.fromCurrency,
        date : req.body.date,
    });
    const options = pythonServerConfig.pythonServerConfig(path = req.path, method = req.method);
    options.headers = {
        'Content-Type': 'application/json',
        'Content-Length': data.length
        };
    httpServer.sendHttpRequest(res, options, data, function(body,data){
        if ((!!body) && (body.constructor === Array)){
            exchangeStorage.add_exchange_history(JSON.parse(data), body);
            if(cross_rates_from_history.length != 0){
                Array.prototype.push.apply(body,cross_rates_from_history);
            }
        }
        res.status = 200;
        res.setHeader('Content-Type', 'application/json');
        return res.json(body);
    });
};
module.exports = {
   exchange
};