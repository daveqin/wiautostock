# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:10:25 2018

@author: Administrator
"""

import talib 
import tushare as ts
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

hist = ts.get_hist_data('002486')


y = hist['close']

close = np.array(y.tolist())

real = talib.SMA(close, timeperiod=30)

x = np.linspace(1,len(real),len(real))
m5 = talib.MA(close, timeperiod=5, matype=0)
m10 = talib.MA(close, timeperiod=10, matype=0)
m30 = talib.MA(close, timeperiod=30, matype=0)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)
plt.plot(x,m5)
plt.plot(x,m10)
plt.plot(x,m30)
plt.plot(x,real)
plt.plot(x,y)




