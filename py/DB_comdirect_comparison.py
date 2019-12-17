#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Import Library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
from pandas.plotting import register_matplotlib_converters

#Gain data from Yahoo Finance
dbank = pd.read_csv('D:\WORK\Anaconda\Dataset\FSE-DBK_X2.csv', parse_dates=True, index_col=0)
comd = pd.read_csv('D:\WORK\Anaconda\Dataset\FSE-COM_X2.csv', parse_dates=True, index_col=0)

#Plotting Stock Prices
dbank['Close'].plot(label='DBK-DeutscheBank',figsize=(10,10))
dbank.reset_index(inplace=True)
dbank.set_index('Date', inplace=True)

comd['Close'].plot(label='COM-comdirectbankAG')
comd.reset_index(inplace=True)
comd.set_index('Date', inplace=True)

plt.xlabel('Date')
plt.ylabel('Closure Price')
plt.title('Deutsche Bank and comdirect bank AG Stock Price Comparison')
plt.legend()
plt.show()


# In[ ]:




