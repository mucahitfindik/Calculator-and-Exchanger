const formula = require('../history/formula')
const exchangeStorage = require("../history/exchange-storage")
const history_formula = async (req, res, next) => {
    const list = formula.formula_history_list;
    return res.json({"formula_history":list});

      
};
const history_exchange = async (req, res, next) => {
    const list = exchangeStorage.exchange_history_list;
    return res.json({"exchange_history":list});

      
};
module.exports = {
    history_formula,
    history_exchange
};