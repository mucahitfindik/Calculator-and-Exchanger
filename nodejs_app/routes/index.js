var express = require('express');
const calculationController  = require('../controllers/calculation');
const exchangeController  = require('../controllers/exchange');
const historyController  = require('../controllers/history');
var router = express.Router();

router.get('/calculate', calculationController.calculation);
router.get('/exchange', exchangeController.exchange);
router.get('/history/formula', historyController.history_formula);
module.exports = router;