import pandas_datareader.data as web
import datetime

start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 8, 1)

facebook = web.DataReader('AAPL', 'yahoo', start, end)
print(facebook.head())
