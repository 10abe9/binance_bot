from binance.spot import Spot


client = Spot(api_key='8V3krxCN6qZwIOaxXRpla2UH2C6SMK98KIsWAjDthmAg4mkuOCDZvUGMQ9khZbvZ', api_secret='ZUoP6eddQHa7GPgw3hygSkjWiiZAy6ViKnq2qA4Uek6DWP6AqtHvEf9zVtxWFR0o')
print(client.account())
# Post a new order
params = {
    'symbol': 'BTCUSDT',
    'side': 'BUY',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 9500
}

response = client.new_order(**params)
print(response)