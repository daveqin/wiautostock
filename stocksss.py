# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 16:05:49 2018

@author: Administrator
"""

import numpy as np
import talib as ta
import tushare as ts


hist_data = ts.get_hist_data('002486',start='2017-01-01')

print hist_data