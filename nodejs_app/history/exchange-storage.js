const exchange_history_list= [];
const add_exchange_history = (request_data, result)=>{
    if (exchange_history_list.length == 0){
        add_new_date_to_array(request_data,result);
    }
    else{
        flag_date_exists = false;
        exchange_history_list.forEach(record_by_date =>{
            if(record_by_date['date'] == request_data.date){
                flag_date_exists = true;
                records_cross_rates = record_by_date["records"];
                result.forEach(item =>{
                    record = create_record(item, request_data);
                    records_cross_rates.push(record);
                })
                return;
            }
        })
        if(!flag_date_exists){
            add_new_date_to_array(request_data,result);
        }
    }
}

const add_new_date_to_array = (request_data, result)=>{
    records_by_date ={}
    records_cross_rates=[]
    result.forEach(item =>{
        record = create_record(item, request_data);
        records_cross_rates.push(record);
    })
    
    records_by_date['date'] = request_data.date;
    records_by_date['records'] = records_cross_rates;
    
    exchange_history_list.push(records_by_date);
}

const create_record = (item, request_data)=>{
    record ={
        to_currency: item.to_currency,
        cross_rate: item.cross_rate,
        from_currency:request_data.fromCurrency,
    };
    return record;

}
module.exports = {
    add_exchange_history,
    exchange_history_list
 };