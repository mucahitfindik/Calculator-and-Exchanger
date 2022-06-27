const formula = require('../history/formula')
const history_formula = async (req, res, next) => {
    const list = formula.formula_history_list;
    return res.json({"formula_history":list});

      
};
module.exports = {
    history_formula
};