const request = require('supertest')
const app = require('../app')
describe('Exchange EndPoint Check', () => {
    it('php_app calculate end point check', async() => {
        const body = {
            "amount" : 120, 
            "toCurrency" : "TRY", 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request("0.0.0.0:5002").get("/exchange").send(body)
        expect(res.statusCode).toEqual(200)
        expect(res.body).toEqual([{ cross_rate: 17.3866, result: 2086.3920000000003, to_currency: 'TRY'}])
    })
    it('should create a request with a body', async() => {
        const body = {
            "amount" : 120, 
            "toCurrency" : "TRY", 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request(app).get("/exchange").send(body)
        
        expect(res.statusCode).toEqual(200)
        expect(res.body).toEqual([{ cross_rate: 17.3866, result: 2086.3920000000003, to_currency: 'TRY'}])
    })
    it('should create a request with a body that has to_currency is a list', async() => {
        const body = {
            "amount" : 120, 
            "toCurrency" : ["TRY", "DKK"], 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request(app).get("/exchange").send(body)
        
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
        const res = await request(app).get("/exchange")
        expect(res.statusCode).toEqual(404)
        expect(res.body.error).toEqual("Request As Not Expected!")
    })
    
  })