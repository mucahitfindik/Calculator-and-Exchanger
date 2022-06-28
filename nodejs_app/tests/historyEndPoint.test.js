const request = require('supertest')
const app = require('../app')
describe('History EndPoint Check', () => {
    it('history/formula end point check', async() => {
        const formula_history = await (await request(app).get("/history/formula")).body.formula_history
        expect(formula_history).toEqual([])
    })
    it('history/formula end point check after send a request to the calculate end point', async() => {
        const body = {
            expression: "2+3+4"
          }
        const res_calculate = await request(app).get("/calculate").send(body)
        const formula_history = await (await request(app).get("/history/formula")).body.formula_history
        expect(formula_history[0]).toEqual({
            expression:body.expression,
            result:res_calculate.body.result
        })
    })
    it('history/exchange end point check', async() => {
        const exchange_history = await (await request(app).get("/history/exchange")).body.exchange_history;
        
        expect(exchange_history).toEqual([])
    })
    it('history/exchange end point check after send a request to the exchange end point', async() => {
        const body = {
            amount : 120, 
            toCurrency : "USD", 
            fromCurrency: "TRY", 
            date:"2022-06-23"
        }
        const res_exchange = await request(app).get("/exchange").send(body)
        const exchange_history = await (await request(app).get("/history/exchange")).body.exchange_history;
        expect(exchange_history[0]).toEqual({
            exchange_request:body,
            result:res_exchange.body
        });
    })
    
  })