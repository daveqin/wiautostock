# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:52:12 2017

@author: Administrator
"""

import math
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt

from httpapi import *





#print data1.to_json(orient='split')

def get_hist(stock):
    
    data=ts.get_hist_data(stock)
    data1=data[['open','high','close','low']]
    
    return data1





port = 5089
httpd = make_server("0.0.0.0", port, application)
print "serving http on port {0}...".format(str(port))
httpd.serve_forever()