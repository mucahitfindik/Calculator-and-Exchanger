const formula_history_list= [];
const add_formula_history = (request_data, result)=>{
    record = {
        calculation_request:request_data,
        result:result
    }
    formula_history_list.push(record);
}
module.exports = {
    add_formula_history,
    formula_history_list
 };