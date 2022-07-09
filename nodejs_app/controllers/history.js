const formula = require('../history/formula')
const exchangeStorage = require("../history/exchange-storage")
const formula_history = formula.formula_history_list;
const exchange_history = exchangeStorage.exchange_history_list;
const history_formula = async (req, res, next) => {
    
    return res.json({"formula_history":formula_history});

      
};
const history_exchange = async (req, res, next) => {
    return res.json({"exchange_history":exchange_history});   
};
const search_formula_history = (data, cb)=>{
    expression = data.expression;
    if(formula_history.length == 0){
        cb(null);
        return;
    }
    let expression_result = null;
    formula_history.every(item =>{
        if(expression == item.expression){
            expression_result = item.result;
            return false;
        }
        return true;
    })
    cb(expression_result);
}

const search_exchange_history_by_date = (data, cb)=>{
    date = data.date
    if(exchange_history.length == 0){
        cb([]);
        return;
    }
    let cross_rates_from_history = []
    exchange_history.every(item =>{
        if(date == item.date){
            get_cross_rate_history_exchange(item.records, data.toCurrency, data.fromCurrency, function(cross_rates){
                cross_rates_from_history = cross_rates;
                return false;
            });
        }
        return true;
    })
    cb(cross_rates_from_history);
};

const get_cross_rate_history_exchange = (records, to_currency, from_currency, cb)=>{
    const cross_rates = []
    records.every(record =>{
        if(record.from_currency == from_currency ){
            to_currency.forEach(currency=>{
                if(record.to_currency == currency){
                    cross_rates.push(record);
                }
            })
            
        }
        else if(record.to_currency == from_currency){
            to_currency.forEach(currency=>{
                if(record.from_currency == currency )
                reverse_record ={
                    to_currency : record.from_currency,
                    cross_rate: 1/record.cross_rate,
                    from_currency: record.to_currency
                };
                cross_rates.push(reverse_record)
            })
            
        }
        if(cross_rates.length == to_currency.length){
            return false;
        }
        return true;
    })
    cb(cross_rates);
};
module.exports = {
    history_formula,
    history_exchange,
    search_exchange_history_by_date,
    search_formula_history
};