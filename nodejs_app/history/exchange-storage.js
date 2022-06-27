const exchange_history_list= [];
const add_exchange_history = (request_data, result)=>{
    record = {
        exchange_request:request_data,
        result:result
    }
    exchange_history_list.push(record);
}
module.exports = {
    add_exchange_history,
    exchange_history_list
 };