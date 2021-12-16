import requests
import smtplib
import time

api_key = '4bc284d6e24d8281c7e6caf04846fd5c'
password = 'Jaguar374'


def price_tracker(api_key,password):
    prices = requests.get(f'https://financialmodelingprep.com/api/v3/quote/AAPL?apikey={api_key}').json()
    stock_price = prices[0]['price']
    print(stock_price)

def send_email(password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jaguar.python11@gmail.com', password)
    subject = 'Apple Price has dropped'
    body = f'It is now {stock_price}'
    msg = f'subject: {subject} {body}'

    server.sendmail(
        'jaguar.python11@gmail.com',
        'jaguar.python11@gmail.com',
        msg
    )
    print('email is sent')
    server.quit()

if stock_price < 140:
    send_email(password)
while (True):
    price_tracker(api_key, password)
    time.sleep(600)