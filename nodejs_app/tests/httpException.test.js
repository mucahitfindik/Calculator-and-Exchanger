const request = require('supertest')
const app = require('../app')

describe('Calculation EndPoint Check', () => {
    it('should create a request with a body to unsupported endpoint', async() => {
        const body = {
            expression: "2+3+4"
          }
        const res = await request(app).post("/calculation").send(body)
        expect(res.statusCode).toEqual(404)
        expect(res.body.error).toEqual("The requested URL was not found on the server.")
    })
    it('should create a request with a body to endpoint with wrong method', async() => {
        const body = {
            "amount" : 120, 
            "toCurrency" : ["USD"], 
            "fromCurrency": "TRY",
            "date": "2022-06-23"
        }
        const res = await request(app).get("/exchange").send(body)
        expect(res.statusCode).toEqual(404)
        expect(res.body.error).toEqual("The requested URL was not found on the server.")
    })
    
})