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

