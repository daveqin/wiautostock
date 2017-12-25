# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:52:12 2017

@author: Administrator
"""

import math
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt






#print data1.to_json(orient='split')

def get_hist(stock):
    
    data=ts.get_hist_data(stock)
    data1=data[['open','high','close','low']]
    
    return data1.to_json(orient='split')


#print get_hist('002486')

