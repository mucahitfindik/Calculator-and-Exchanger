const request = require('supertest')
const app = require('../app')
describe('Exchange EndPoint Check', () => {
    it('php_app calculate end point check', async() => {
        const body = {
            "amount" : 120, 
            "toCurrency" : ["TRY"], 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request("0.0.0.0:5002").post("/exchange").send(body)
        expect(res.statusCode).toEqual(200)
        expect(res.body).toEqual([{ cross_rate: 17.3866, result: 2086.3920000000003, to_currency: 'TRY'}])
    })
    it('should create a request with a body', async() => {
        const body = {
            "amount" : 120, 
            "toCurrency" : ["TRY"], 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request(app).post("/exchange").send(body)
        
        expect(res.statusCode).toEqual(200)
        expect(res.body).toEqual([{ cross_rate: 17.3866, result: 2086.3920000000003, to_currency: 'TRY'}])
    })
    it('should response to the request using history', async() => {
        const body = {
            "amount" : 120, 
            "toCurrency" : ["TRY"], 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res_ = await request(app).post("/exchange").send(body)
        const res = await request(app).post("/exchange").send(body)

        
        expect(res.statusCode).toEqual(200)
        expect(res.body).toEqual([{ cross_rate: 17.3866, result: 2086.3920000000003, to_currency: 'TRY'}])
    })
    it('should response to the request using history by changing fromCurrency to toCurrency vice versa', async() => {
        const body_ = {
            "amount" : 120, 
            "toCurrency" : ["TRY"], 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res_ = await request(app).post("/exchange").send(body_)
        const body = {
            "amount" : 120, 
            "toCurrency" : ["USD"], 
            "fromCurrency": "TRY",
            "date": "2022-06-23"
        }
        const res = await request(app).post("/exchange").send(body)

        expect(res.statusCode).toEqual(200)
        expect(res.body).toEqual([{ cross_rate: 0.05751555795842775, result: 6.90186695501133, to_currency: 'USD'}])
    })
    it('should create a request with a body that has to_currency is a list', async() => {
        const body = {
            "amount" : 120, 
            "toCurrency" : ["TRY", "DKK"], 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request(app).post("/exchange").send(body)
        expect(res.statusCode).toEqual(200)
        expect(res.body).toEqual([
            {
                cross_rate: 7.0734,
                result: 848.808,
                to_currency: "DKK"
            },
            {
                cross_rate: 17.3866,
                result: 2086.3920000000003,
                to_currency: "TRY"
            }
        ])
    })
    it('should create a request without a body', async() => {
        const res = await request(app).post("/exchange")
        expect(res.statusCode).toEqual(400)
        expect(res.body.error).toEqual("No amount provided!")
    })
    it('should create a request with a body that does not include amout attribute', async() => {
        const body = {
            "toCurrency" : ["TRY", "DKK"], 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request(app).post("/exchange").send(body)
        expect(res.statusCode).toEqual(400)
        expect(res.body.error).toEqual("No amount provided!")
    })
    it('should create a request with a body that amount is not number', async() => {
        const body = {
            "amount": "",
            "toCurrency" : ["TRY", "DKK"], 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request(app).post("/exchange").send(body)
        expect(res.statusCode).toEqual(400)
        expect(res.body.error).toEqual("Amount should be number!")
    })
    it('should create a request with a body that does not include toCurrency attribute', async() => {
        const body = {
            "amount": 120,
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request(app).post("/exchange").send(body)
        expect(res.statusCode).toEqual(400)
        expect(res.body.error).toEqual("Please select the currency(s) in which you want to exchange the amount.")
    })
    it('should create a request with a body that toCurrency is empty array', async() => {
        const body = {
            "amount": 120,
            "toCurrency" : [], 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request(app).post("/exchange").send(body)
        expect(res.statusCode).toEqual(400)
        expect(res.body.error).toEqual("Please select the currency(s) in which you want to exchange the amount.")
    })
    it('should create a request with a body that toCurrency is not an array ', async() => {
        const body = {
            "amount": 120,
            "toCurrency" : 'TRY', 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request(app).post("/exchange").send(body)
        expect(res.statusCode).toEqual(400)
        expect(res.body.error).toEqual("toCurrency should be array!")
    })
    it('should create a request with a body that does not include fromCurrency attribute', async() => {
        const body = {
            "amount": 120,
            "toCurrency" : ["SEK"], 
            "date": "2022-06-23"
        }
        const res = await request(app).post("/exchange").send(body)
        expect(res.statusCode).toEqual(400)
        expect(res.body.error).toEqual("Please select a currency of the amount.")
    })
    it('should create a request with a body that fromCurrency is empty', async() => {
        const body = {
            "amount": 120,
            "toCurrency" : ["SEK"],
            "fromCurrency": "", 
            "date": "2022-06-23"
        }
        const res = await request(app).post("/exchange").send(body)
        expect(res.statusCode).toEqual(400)
        expect(res.body.error).toEqual("Please select a currency of the amount.")
    })
    it('should create a request with a body that fromCurrency is not a string', async() => {
        const body = { 
            "amount": 120,
            "toCurrency" : ["TRY"], 
            "fromCurrency": [],
            "date": "2022-06-23"
        }
        const res = await request(app).post("/exchange").send(body)
        expect(res.body.error).toEqual("fromCurrency should be string!")
    })
    it('should create a request with a body that does not include date attribute ', async() => {
        const body = {
            "amount": 120,
            "toCurrency" : ["TRY"], 
            "fromCurrency": "USD",
        }
        const res = await request(app).post("/exchange").send(body)
        expect(res.statusCode).toEqual(400)
        expect(res.body.error).toEqual("No date provided!")
    })
    it('should create a request with a body that date is empty ', async() => {
        const body = {
            "amount": 120,
            "toCurrency" : ["TRY"], 
            "fromCurrency": "USD",
            "date": ""
        }
        const res = await request(app).post("/exchange").send(body)
        expect(res.statusCode).toEqual(400)
        expect(res.body.error).toEqual("No date provided!")
    })
    
  })