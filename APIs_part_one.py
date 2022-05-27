import pandas as pd
import numpy as numpy
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
#from mplfinance.original_flavor import candlestick2_ohlc

test_data = {'a' : [11,19,23,27,29,31, 35], 'b' : [2,4,6,8,10,12,14], 'c' : [3,9,12,13,14,15,16]}

df = pd.DataFrame(test_data)

# get info on dataframe
print "Type:", type(df)
print "First rows:"
print df.head()
print "Column means:" 
print df.mean()

# REST API

cg = CoinGeckoAPI()
bc_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# get info on API object
print "Data of type: ", type(bc_data)
for key in bc_data:
	print key

price_data = bc_data['prices']
print "Price data of type: ", type(price_data)
print "First five elements of price data: ", price_data[0:5]

# store in dataframe
prices = pd.DataFrame(price_data, columns=['Timestamp', 'Price'])

# convert time using datetime module
prices['date'] = prices['Timestamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

# make candlestick plot, grouping by date
candlestick_data = prices.groupby(prices.date, as_index=False).agg({'Price': ['min', 'max', 'first', 'last']})
fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],open=candlestick_data['Price']['first'],high=candlestick_data['Price']['max'], low=candlestick_data['Price']['min'],close=candlestick_data['Price']['last'])])

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()


