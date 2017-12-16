# -*- coding: gb2312-*-
"""
Created on Fri Nov 17 15:41:57 2017

@author: Administrator
"""

import datetime
import time
from winautos import main_buy,main_SellS
from SenEmil  import SenEmails
from analysisStock import stock_ma60



def doSth():
    SenEmails(u'start',u'start')
    #go go start do thing
    #anaysis stock 
    time.sleep(30)
    res = stock_ma60('000651')  
    res2 = stock_ma60('000002') 
    res3 = stock_ma60('600887')
    if res=='buy':
        #main_buy('000651','2.2','200')
        SenEmails(u'start',u'buy 000651')
    else:
        SenEmails(u'start',u'not buy 000651 stock')
    
    if res2=='buy':
        #main_buy('000002','0','200')
        SenEmails(u'start',u'buy 000002')
    else:
        SenEmails(u'start',u'not buy 000002 stock')
        
    if res3=='buy':
        #main_buy('600887','0','200')
        SenEmails(u'start',u'buy 600887')
    else:
        SenEmails(u'start',u'not buy 600887 stock')   
        
    time.sleep(60)

def main(h=0, m=0):
    '''h  express hour        express min'''
    workTime = range(5)       #make work time [0,1,2,3,4]
    d=datetime.datetime.now() #get now time
    weekday =  d.weekday()    #get week
    while True:
        # determine whether the set time ,such as 0:0
        if weekday in workTime:
            while True:
                now = datetime.datetime.now()
                # The time  up does the thing
                if now.hour==h and now.minute==m:
                    break
                # no time ,sleep 30s
                time.sleep(10)
            # do thing ,one day one to make
            
            doSth()

main(h=14,m=50)







#Fri