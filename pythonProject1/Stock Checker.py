import requests

stock_ticker = input()

def stock_tracker(stock_ticker):
    prices = requests.get(f'https://financialmodelingprep.com/api/v3/quote/{stock_ticker}?apikey=4bc284d6e24d8281c7e6caf04846fd5c').json()
    stock_price = prices[0]['price']
    bought_price = int(input())
    price_change = stock_price - bought_price
    if (price_change > 0):
        print (stock_price - bought_price)
        print (stock_ticker + " stock is up")
    else:
        print(stock_price - bought_price)
        print(stock_ticker + " stock is down")

stock_tracker(stock_ticker)