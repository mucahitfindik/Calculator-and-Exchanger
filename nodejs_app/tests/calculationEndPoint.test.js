const request = require('supertest')
const app = require('../app')
const phpServerConfig = require("../controllers/phpServerConfig")
const sendHttp = require("../controllers/httpServer")

describe('Calculation EndPoint Check', () => {
    it('php_app calculate end point check', async() => {
        const body = {
            expression: "(2/4*(6-3))"
          }
        const res = await request("0.0.0.0:8002").get("/calculate").send(body)
        expect(res.statusCode).toEqual(200)
        expect(res.body.result).toEqual(1.5)
    })
    it('should create a request with a body which includes expression', async() => {
        const body = {
            expression: "2+3+4"
          }
        const res = await request(app).get("/calculate").send(body)
        expect(res.statusCode).toEqual(200)
        expect(res.body.result).toEqual(9)
    })
    it('should create a request without a body', async() => {
        const res = await request(app).get("/calculate")
        expect(res.statusCode).toEqual(404)
        expect(res.body.error).toEqual("Expression Not Found!")
    })
    
  })