var express = require('express');
const calculationController  = require('../controllers/calculation');
const exchangeController  = require('../controllers/exchange');
var router = express.Router();

router.get('/calculate', calculationController.calculation);
router.get('/exchange', exchangeController.exchange);
module.exports = router;