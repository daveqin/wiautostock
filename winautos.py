# -*- coding: gb2312 -*- 

import sys
reload(sys)

from config import VK_CODE
from comm import writTxt
#from pywinauto import application
import win32clipboard as wc
from pykeyboard import PyKeyboard
import win32gui, win32api, win32con 
import time



class Winauto(object):
   
    def __init__(self):
        self.k = PyKeyboard() #get pykeyboard        
        self.software= u'网上股票交易系统5.0'
        self.hWndChildList=0
        fileext = u'C:\\同花顺软件\\同花顺\\xiadan.exe'    
        ver     = 'ver=1 "0711296a70d754486417e81e747c6d7a72c8e267d205855f3789557393017109896345c0fc9952107eadf3e65a87dbe90b74d87f23c775a3f4fafed32aaca87e"'
        self.password = '192351'
        #open sofware
        
        #self.appStart(fileext,ver)
		
        self.para_hld=win32gui.FindWindow(None,self.software) #get hld by app word
        
        
        if self.para_hld<=0:
            self.appStart(fileext,ver)
        
        time.sleep(2)
        if self.para_hld>0:
            win32gui.SetForegroundWindow(self.para_hld)  #show window
            self.hWndChildList=self.demo_child_windows(self.para_hld) #get hld 
            attr=self.show_window_attr(self.para_hld)
            #print attr
            win32api.SetCursorPos([attr['post'][0],attr['post'][1]]) #Mover to post(x,y)
			
        
        
    '''
    ldList:
    'post:?§|left, top, right, bottom 
    '''

    def GetHld(self,post):
        
        for hld in self.hWndChildList:
            left, top, right, bottom =win32gui.GetWindowRect(hld) #get hld post left top right bottom
            #if (post[0]==left) & (post[1]==top) & (post[2]==right) & (post[3]==right):
           
            if (post[0]==left) & (post[1]==top): #get hld by (x,y) left top
                 return hld
        return 0

    def GetHldWord(self,word):
         for hld in self.hWndChildList:
            
            title = win32gui.GetWindowText(hld) 
            title=title.decode('gbk')
            if title==word:
                 return hld
         return 0
    
	#get all demo chlid hld window
    def demo_child_windows(self,parent):  
      
        if not parent:  
            return  
        hWndChildList = []  
        win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd),  hWndChildList)  
       
        return hWndChildList  
    ''''' 
   
    :return: 
    '''  
    
	#get all hld attr
    def show_window_attr(self,hWnd):  
        if not hWnd:  
            return  
       
        title = win32gui.GetWindowText(hWnd)  
        clsname = win32gui.GetClassName(hWnd) 
        left, top, right, bottom =win32gui.GetWindowRect(hWnd) #
        attr = {'hWnd':hWnd,'title': title, 'clsname':clsname, 'post':[left,top,right,bottom]}    
    
        return attr 
        
        
    #buy a stock parameter stock price nun
    def BuyS(self,buy_stock,buy_price,buy_nun):
         win32api.keybd_event(VK_CODE['F1'],0,0,0) #F2
         self.k.type_string(buy_stock)       
         win32api.keybd_event(VK_CODE['tab'],0,0,0) #   
         time.sleep(2)
         if buy_price!='0':        
            self.k.type_string(buy_nun) 
         #k.type_string(buy_price) 
         win32api.keybd_event(VK_CODE['tab'],0,0,0) #
         self.k.type_string(buy_nun)                #
         win32api.keybd_event(VK_CODE['enter'],0,0,0) #
         win32api.keybd_event(VK_CODE['enter'],0,0,0) #
    
        
	
    def SellS(self,buy_stock,buy_price,buy_nun):
        
         win32api.keybd_event(VK_CODE['F2'],0,0,0)  #
         self.k.type_string(buy_stock)              #import stock
         win32api.keybd_event(VK_CODE['tab'],0,0,0) #import tab  
         time.sleep(2)#                                 #sleep 2s
         if buy_price!='0':
             self.k.type_string(buy_price) 
         win32api.keybd_event(VK_CODE['tab'],0,0,0)  
         self.k.type_string(buy_nun) 
         win32api.keybd_event(VK_CODE['enter'],0,0,0) 
         time.sleep(2)
         win32api.keybd_event(VK_CODE['enter'],0,0,0) 
       
    
    def getAllAsset(self):
        
        
        win32api.keybd_event(VK_CODE['F4'],0,0,0)  #
        distance = 54 #left_distance
        balance      = u'资金余额'
        balance      =self.getSset(balance,distance)
        othe_balance = u'可用金额'
        othe_balance =self.getSset(othe_balance,distance)
        market_value = u'股票市值'
        market_value =self.getSset(market_value,distance)
        propertys = u'总 资 产'
        propertys =self.getSset(propertys,distance)

        AssetList={'balance':balance['title'],'othe_balance':othe_balance['title'],'market_value':market_value['title'],'propertys':propertys['title']}
        
        return AssetList
        
    def getSset(self,word,distance):
        hld  = self.GetHldWord(word) 
        attr     = self.show_window_attr(hld)
        hld  = self.GetHld((attr['post'][0]+distance,attr['post'][1]))
        attr     = self.show_window_attr(hld)
        
        return attr
        
	#start app go go go
    def appStart(self,fileext,ver):
            
        win32api.ShellExecute(0, 'open',fileext,ver,'',1)       
        time.sleep(10)
        self.k.type_string(self.password)
        win32api.keybd_event(VK_CODE['tab'],0,0,0) 
        win32api.keybd_event(VK_CODE['enter'],0,0,0)
        
    def copyKey(self):
         
        win32api.keybd_event(VK_CODE['ctrl'],0,0,0)      # Alt
        win32api.keybd_event(VK_CODE['c'],0,0,0)        # O
        win32api.keybd_event(VK_CODE['c'],0,win32con.KEYEVENTF_KEYUP,0)  #
        win32api.keybd_event(VK_CODE['ctrl'],0,win32con.KEYEVENTF_KEYUP,0)		


    def getAllStock(self):
        
           win32api.keybd_event(VK_CODE['F4'],0,0,0)
           attr = self.show_window_attr(self.para_hld)
           x = attr['post'][0]+300
           y = attr['post'][1]+300
           win32api.SetCursorPos([x,y]) #Mover to post(x,y)
           self.copyKey()                                                  #copy crtl+f4
           
           copy_txt = self.getCopyText()          							#get copy txt
           copy_txt = copy_txt.rstrip().split("\n") 
           c = []
           cArray = {}
           cloun =  ''
            
           for vv in  copy_txt:
                cloun =  vv.split("	") #split one 
                for v in cloun:        #get vlaue 
                    c.append(v)
                cArray[c[1]]=c         #add list into dicitonary
                c=[]                   #clear all data
           return cArray
		     
    #get copy text              
    def getCopyText(self):
            wc.OpenClipboard()
            copy_text = wc.GetClipboardData(win32con.CF_TEXT)
            wc.CloseClipboard()
            return copy_text	

    
    def closApp(self):
          writTxt('x.txt',str(self.para_hld))
          self.para_hld=win32gui.FindWindow(None,self.software) #get hld by app word
        
          win32gui.PostMessage(self.para_hld, win32con.WM_CLOSE, 0, 0)
       
#kk = Winauto()  
#k=kk.getAllStock()
#writTxt('x.txt',str(len(k)))
#time.sleep(2)
#kk.closApp()
#kk.SellS('600663','0','1000')

    
#kk = Winauto()

def main_buy(stock,price,nun):

	kk = Winauto()
	AssetList=kk.getAllAsset()
	value = AssetList['othe_balance']  #balance
	price = price                         
	nun = int(value/(price*100))*100      #can buy stock nun
	kk.BuyS(stock,price,nun)
	time.sleep(60)
	kk.closApp()                      #close app
	
def main_SellS(stock,price,nun):

	 kk = Winauto() ;time.sleep(2)
	#AssetList=kk.getAllAsset()
	#value = AssetList['othe_balance']  #balance
	#price = price                         
	#nun = int(value/(price*100))*100      #can buy stock nun
   
	 kk.SellS(stock,price,nun)
	 time.sleep(10)
	 kk.closApp()                      #close app
	

#main_SellS('000651','0','200')
#kk.BuyS('600663','0','1000') 
#kk.SellS('600663','0','1000')
#alla=kk.getAllAsset()
#print alla


      