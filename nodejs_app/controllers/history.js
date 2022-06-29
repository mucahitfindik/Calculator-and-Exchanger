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

const search_history_exchange_by_date = (data, cb)=>{
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
                record.cross_rate = 1/record.cross_rate;
                cross_rates.push(record)
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
    search_history_exchange_by_date
};