# -*- coding: gb2312 -*- 
"""
Created on Tue Nov 14 15:02:18 2017

@author: Administrator
"""

import urllib 
import urllib2 

url = "http://127.0.0.1:889"

def getrq(url):
    req = urllib2.Request(url) 
    print req 
    res_data = urllib2.urlopen(req) 
    res = res_data.read() 
    print res 

def postrq():
    test_data = {'action':'buy','nun':'1000','price':'1000','stock':'000242'} 
    test_data_urlencode = urllib.urlencode(test_data) 
    requrl = "http://127.0.0.1:889"
    req = urllib2.Request(url = requrl,data =test_data_urlencode) 
    print req 
    res_data = urllib2.urlopen(req) 
    res = res_data.read() 
    print res 
    

postrq()




