import PySimpleGUI as sg
import requests

layout = [
    [sg.Text('Please enter stock ticker you want to track')],
    [sg.Text('Stock Ticker', size=(15, 1)), sg.InputText()],
    [sg.Button('Save'), sg.Button('Close')]
]
window = sg.Window('Stock Tracker', layout)

layout2 = [
    [sg.Text('Bought Price', size=(15, 1)), sg.InputText()],
    [sg.Text('Number of Stocks', size=(15, 1)), sg.InputText()],
    [sg.Text('Other Income', size=(15, 1)), sg.InputText()],
    [sg.Text('Other Expense', size=(15, 1)), sg.InputText()],
    [sg.Button('Check'), sg.Button('Close')]
]
window = sg.Window('Stock Data', layout2)

event, values = window.read()
stock_ticker = values[0]
bought_price = values[1]
num_stock = values[2]
income = values[3]
expense = values[4]
bought_price_f = float(bought_price)
num_stock_f = float(num_stock)
income_f = float(income)
expense_f = float(expense)

f = open(f'{stock_ticker}.txt', "w+")
f.write(stock_ticker + "\n")
f.write(bought_price + "\n")
f.write(num_stock + "\n")
f.write(income + "\n")
f.write(expense + "\n")
f.close()

def stock_tracker(stock_ticker, bought_price_f, num_stock_f, income_f, expense_f):
    prices = requests.get(f'https://financialmodelingprep.com/api/v3/quote/{stock_ticker}?apikey=4bc284d6e24d8281c7e6caf04846fd5c').json()
    stock_price = prices[0]['price']
    price_change = stock_price - bought_price_f
    total_amount_p = (num_stock_f * stock_price) - (num_stock_f * bought_price_f) + income_f - expense_f
    total_amount_n = (num_stock_f * bought_price_f) - (num_stock_f * stock_price) + income_f - expense_f
    if (price_change > 0):
        sg.popup(f'{stock_price}',f'change is {price_change}',f'{stock_ticker} stock is up', f'{total_amount_p} is the total amount you made')
        print(stock_price)
        print(price_change)
        print(stock_ticker + " stock is up")
        print(total_amount_p + " is the total amount you made")
    else:
        sg.popup(f'{stock_price}', f'change is {price_change}', f'{stock_ticker} stock is down', f'{total_amount_n} is the total amount you lost')
        print(stock_price)
        print(price_change)
        print(stock_ticker + " stock is down")
        print(total_amount_n + " is the total amount you lost")

if event == sg.WIN_CLOSED:
    window.close()
elif event == 'Check':
    stock_tracker(stock_ticker, bought_price_f, num_stock_f, income_f, expense_f)
elif event == 'Close':
    window.close()

window.close()