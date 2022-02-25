var express = require('express');
const calculationController  = require('../controllers/calculation');
var router = express.Router();

router.get('/calculate', calculationController.calculation);
module.exports = router;