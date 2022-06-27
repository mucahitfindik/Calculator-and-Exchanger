const formula_history_list= [];
const add_formula_history = (formula, result)=>{
    record = {
        formula:formula,
        result:result
    }
    formula_history_list.push(record);
}
module.exports = {
    add_formula_history,
    formula_history_list
 };