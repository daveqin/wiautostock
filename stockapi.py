# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:52:12 2017

@author: Administrator
"""

import math
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt

import json


data=ts.get_hist_data('600848')
data1=data[['open','high','close','low']]

print data1.to_json(orient='split')