const request = require('supertest')
const app = require('../app')
describe('History EndPoint Check', () => {
    it('check history/formula end point', async() => {
        const formula_history = await (await request(app).get("/history/formula")).body.formula_history
        expect(formula_history).toEqual([])
    })
    it('check history/formula end point after send a request to the calculate end point', async() => {
        const body = {
            expression: "2+3+4"
          }
        const res_calculate = await request(app).post("/calculate").send(body)
        const formula_history = await (await request(app).get("/history/formula")).body.formula_history
        expect(formula_history[0]).toEqual({
            expression:body.expression,
            result:res_calculate.body.result
        })
    })
    it('check history/exchange end point', async() => {
        const exchange_history = await (await request(app).get("/history/exchange")).body.exchange_history;
        
        expect(exchange_history).toEqual([])
    })
    it('checkhistory/exchange end point after send a request to the exchange end point', async() => {
        const body = {
            amount : 120, 
            toCurrency : ["USD"], 
            fromCurrency: "TRY", 
            date:"2022-06-23"
        }
        const res_exchange = await request(app).post("/exchange").send(body)
        const exchange_history = await (await request(app).get("/history/exchange")).body.exchange_history;
        expect(exchange_history[0]).toEqual( {
            date: body.date,
            records: [
                {
                    to_currency: body.toCurrency[0],
                    cross_rate: res_exchange.body[0]["cross_rate"],
                    from_currency: body.fromCurrency
                }
            ]
        });
    })
    it('checkhistory/exchange end point after send a request to the exchange end point with multi to_currency', async() => {
        const body = {
            amount : 120, 
            toCurrency : ["USD", "DKK"], 
            fromCurrency: "TRY", 
            date:"2022-06-24"
        }
        const res_exchange = await request(app).post("/exchange").send(body)
        const exchange_history = await (await request(app).get("/history/exchange")).body.exchange_history;
        expect(exchange_history[1]).toEqual( {
            date: body.date,
            records: [
                {
                    to_currency: body.toCurrency[0],
                    cross_rate: res_exchange.body[0]["cross_rate"],
                    from_currency: body.fromCurrency
                },
                {
                    to_currency: body.toCurrency[1],
                    cross_rate: res_exchange.body[1]["cross_rate"],
                    from_currency: body.fromCurrency
                }
            ]
        });
    })
    
  })