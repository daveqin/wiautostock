# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:52:12 2017

@author: Administrator
"""

import math
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt




class stockapi:
    def __init__(self,stock ):
        self.stock = stock
    
    def get_hist(self):
        
        data=ts.get_hist_data(self.stock)
        data1=data[['open','high','close','low']]
        
        return data1.to_json(orient='split')
        
    def get_mac(self):
        
#print data1.to_json(orient='split')


st = stockapi("002486")
print st.get_hist()


#print get_hist('002486')

