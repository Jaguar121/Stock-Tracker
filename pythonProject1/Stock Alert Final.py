import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
import smtplib


def AlertFinder(data):
    # in this function we find if stock is below certain moving average
    # if yes, we will trigger alert for this stock
    data['MA100'] = data['Close'].rolling(window=100).mean()
    data['Alert'] = np.nan
    Index = data[data.Close < data.MA100].index
    data.loc[Index, 'Alert'] = 1
    return data


# importing watchlist
symbols = pd.read_csv('watchlist.csv')
symbols = list(symbols.Symbols.values)

end = datetime.datetime.today()
start = end - datetime.timedelta(days=500)
alerts = []
for symbol in symbols:
    print(symbol)
    data = web.DataReader(symbol, 'yahoo', start, end)
    data = AlertFinder(data)
    if data['Alert'].iloc[-1] == 1:
        alerts.append(symbol)

gmail_user = 'jaguar.python11@gmail.com'
gmail_password = 'Jaguar374'

if len(alerts) > 0:
    # we have some alerts to send
    Text = 'Following stock alert are triggered: '
    for j in range(len(alerts)):
        Text = Text + ' ' + alerts[j] + ', '

    email_text = 'Subject: {}\n\n{}'.format('--> Daily Stock Alerts', Text)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        print('Logged in Gmail, sending email now')
        server.sendmail(gmail_user, gmail_user, email_text)
        server.close()

    except:
        print('Failed to login')