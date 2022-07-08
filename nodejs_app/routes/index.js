var express = require('express');
const calculationController  = require('../controllers/calculation');
const exchangeController  = require('../controllers/exchange');
const currency_listController  = require('../controllers/currency-list');
const historyController  = require('../controllers/history');
var router = express.Router();

router.post('/calculate', calculationController.calculation);
router.post('/exchange', exchangeController.exchange);
router.get('/currency-list', currency_listController.currency_list);
router.get('/history/formula', historyController.history_formula);
router.get('/history/exchange', historyController.history_exchange);

router.use('*', function(req, res){
    res.status(404).json({"error":"The requested URL was not found on the server."});
  });
module.exports = router;