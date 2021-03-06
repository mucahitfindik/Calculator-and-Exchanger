const request = require('supertest')
const app = require('../app')

describe('Calculation EndPoint Check', () => {
    it('php_app calculate end point check', async() => {
        const body = {
            expression: "(2/4*(6-3))"
          }
        const res = await request("0.0.0.0:8002").post("/calculate").send(body)
        expect(res.statusCode).toEqual(200)
        expect(res.body.result).toEqual(1.5)
    })
    it('should create a request with a body which includes expression', async() => {
        const body = {
            expression: "2+3+4"
          }
        const res = await request(app).post("/calculate").send(body)
        expect(res.statusCode).toEqual(200)
        expect(res.body.result).toEqual(9)
    })
    it('should create a request without a body', async() => {
        const res = await request(app).post("/calculate")
        expect(res.statusCode).toEqual(400)
        expect(res.body.error).toEqual("Please enter expression")
    })
    it('should response to the request using history', async() => {
      const body = {
          expression: "2+3+4"
        }
      const res_ = await request(app).post("/calculate").send(body)
      const res = await request(app).post("/calculate").send(body)
      expect(res.statusCode).toEqual(200)
      expect(res.body.result).toEqual(9)
  })
    
  })