import PySimpleGUI as sg
import requests

layout = [
    [sg.Text('Please enter stock ticker and price you bought it at')],
    [sg.Text('Stock Ticker', size=(15, 1)), sg.InputText()],
    [sg.Text('Bought Price', size=(15, 1)), sg.InputText()],
    [sg.Button('Check'), sg.Button('Close')]
]

window = sg.Window('Stock Viewer', layout)

event, values = window.read()
stock_ticker = values[0]
bought_price = values[1]
bought_price_f = float(bought_price)

def stock_tracker(stock_ticker, bought_price_f):
    prices = requests.get(f'https://financialmodelingprep.com/api/v3/quote/{stock_ticker}?apikey=4bc284d6e24d8281c7e6caf04846fd5c').json()
    stock_price = prices[0]['price']
    price_change = stock_price - bought_price_f
    if (price_change > 0):
        sg.popup(f'{stock_price}',f'change is {price_change}',f'{stock_ticker} stock is up')
        print(stock_price)
        print(price_change)
        print(stock_ticker + " stock is up")
    else:
        sg.popup(f'{stock_price}', f'change is {price_change}', f'{stock_ticker} stock is down')
        print(stock_price)
        print(price_change)
        print(stock_ticker + " stock is down")

if event == sg.WIN_CLOSED:
    window.close()
elif event == 'Check':
    stock_tracker(stock_ticker, bought_price_f)
elif event == 'Close':
    window.close()

window.close()