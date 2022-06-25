const request = require('supertest')
const app = require('../app')
const pythonServerConfig = require("../controllers/pythonServerConfig")
const sendHttp = require("../controllers/httpServer")
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
        expect(res.body.result).toEqual(6.9)
    })
    it('should create a request with a body which includes expression', async() => {
        const body = {
            "amount" : 120, 
            "toCurrency" : "TRY", 
            "fromCurrency": "USD",
            "date": "2022-06-23"
        }
        const res = await request(app).get("/exchange").send(body)
        expect(res.statusCode).toEqual(200)
        expect(res.body.result).toEqual(6.9)
    })
    it('should create a request without a body', async() => {
        const res = await request(app).get("/exchange")
        expect(res.statusCode).toEqual(404)
        expect(res.body.error).toEqual("Request As Not Expected!")
    })
    
  })