# -*- coding: gb2312 -*- 
"""
Created on Fri Nov 10 13:20:19 2017

@author: Administrator
"""


''''' 
Created on 2015-7-20 
 
@author: xhw 
 
@explain: ʵ��GET������POST�������� 
'''  
from  BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler  
from winautos import Winauto 
import urllib  
import os
import time
  
class ServerHTTP(BaseHTTPRequestHandler):
    #�����Ʊ����
    def BuySock(self,stock,price,nun):
        auto = Winauto()  #ʵ����
        auto.BuyS(stock,'0',nun)  #ִ�в���
       
        print '�����Ʊ'
    
    #������Ʊ����    
    def SellSock(self,stock,price,nun):
        #auto = Winauto()  #ʵ����
        #auto.SellS(stock,'0',nun)  #ִ�в���
        
        print '������Ʊ����'
        
    #�ж�Ҫִ�еĲ���
    def Action(self,action,datas):
        if (datas['stock']!=0) & (datas['price']!=0) & (datas['nun']!=0):
         
            if action=='buy':
                self.BuySock(datas['stock'],datas['price'],datas['nun'])
            elif action=='sell':
                self.SellSock(datas['stock'],datas['price'],datas['nun'])
            
  
      
      
    #���ݿ����������
    def Postdata(self,datas):
        dat={}
        datalist = datas.split('&')
        for i in datalist:
           d=i.split('=')
           dat[d[0]]=d[1]
          
          
        return dat   
  
        
    def do_GET(self):  
        path = self.path  
        
        print path  
        #���url(Ҳ�ɸ��ݲ�ֵ�url��ȡGet�ύ������),���Խ���ͬ��path�Ͳ������ز�ͬ��htmlҳ�棬����ò�ͬ�ķ������ز�ͬ�����ݣ���ʵ�ּ򵥵���վ��ӿ�  
        query = urllib.splitquery(path)  
        print query  
        self.send_response(200)  
        self.send_header("Content-type","text/html")  
        self.send_header("test","This is test!")  
        self.end_headers()  
        buf = '''''<!DOCTYPE HTML> 
                <html> 
                <head><title>Get page</title></head> 
                <body> 
                 
                <form action="post_page" method="post"> 
                  action:   <input type="text" name="action" /><br /> 
                  stock: <input type="text" name="stock" /><br /> 
                  price: <input type="text" name="price" /><br /> 
                  nun:   <input type="text" name="nun" /><br /> 
                  <input type="submit" value="POST" /> 
                </form> 
                 
                </body> 
                </html>'''  
        self.wfile.write(buf)  
   
    def do_POST(self):  
        path = self.path  
        print path  
        mpath,margs=urllib.splitquery(self.path)  
        #��ȡpost�ύ������  
        datas = self.rfile.read(int(self.headers['content-length']))  
        datas = urllib.unquote(datas).decode("utf-8", 'ignore') 
        datas = self.Postdata(datas)
        print datas
        if 'action' in datas.keys():
            if datas['action']!='':
                self.Action(datas['action'],datas)
                
            self.retAction(datas,path)
        #�򿪳���
       
    def retAction(self,data,path):
         #self.do_action(mpath, datas) 
       
        self.send_response(200)  
        self.send_header("Content-type","text/html")  
        self.send_header("test","This is test!")  
        self.end_headers()  
        
        buf = '''''<!DOCTYPE HTML> 
        <html> 
            <head><title>Post page</title></head> 
            <body>Post Data:%s  <br />Path:%s</body> 
        </html>'''%(data,self.path)  
        self.wfile.write(buf) 
      
        
        
          
def start_server(port):  
    http_server = HTTPServer(('0.0.0.0', int(port)), ServerHTTP) 
   
    http_server.serve_forever()   
      
if __name__ == "__main__": 
    
    start_server(889)  
  
    