import PySimpleGUI as sg
import requests

stock_ticker = input()
bought_price = int(input())

def stock_tracker(stock_ticker, bought_price):
    prices = requests.get(f'https://financialmodelingprep.com/api/v3/quote/{stock_ticker}?apikey=4bc284d6e24d8281c7e6caf04846fd5c').json()
    stock_price = prices[0]['price']
    price_change = stock_price - bought_price
    if (price_change > 0):
        print (stock_price - bought_price)
        print (stock_ticker + " stock is up")
    else:
        print(stock_price - bought_price)
        print(stock_ticker + " stock is down")

layout = [[sg.Text('Stock Viewer')],
          [sg.Button('Stocks')]]

window = sg.Window('Button Callback Simulation', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Stocks':
        stock_tracker(stock_ticker, bought_price)       # call the "Callback" function

window.close()