# -*- coding: utf-8 --*--
"""
Created on Thu Jan 11 16:28:18 2018

@author: Administrator
"""

#!/usr/bin/env python


from os import path
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
from stockapi import stockapi

import random

curdir = path.dirname(path.realpath(__file__))
sep = '/'

# MIME-TYPE

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    
    def do_action(self,action,stock):
   
        st    = stockapi(stock)
        datas = ""
        #获取历史数据
        if action=='get_hist':
           datas =st.get_hist()
           
        #获取k线图与拆线图
        if action=='get_hist_k':
           #datas_k =st.get_clos()
           datas =st.get_hist_k()
          
        #获取成交量   
        if action=='get_nun':
           datas =st.get_nun() 
           
           
        #获取收盘价格 
        if action=='get_close':
           datas =st.get_clos()
           
           
        #获取涨幅
        if action=='get_change':
           datas =st.get_change()
           
           
         #获取行情数据   
        if action=='get_all':
           datas =st.get_all()
           
        
        return datas
    # GET
    def do_GET(self):
        sendReply = False
        #querypath = parse.urlunparse(self.path)
        #filepath, query = querypath.path, querypath.query
        
        parseResult = parse.urlparse(self.path)
        param_dict = parse.parse_qs(parseResult.query) 
        action = param_dict['action'][0]
        stock  = param_dict['stock'][0]
       
        data = self.do_action(action,stock)
        
       
        #self.send_response('11')
        
   
        self.send_response(200)
        self.send_header('Content-type','ss')
        self.end_headers()
        self.wfile.write(data.encode("utf-8"))
        #self.send_error(404,'111111111111')
        
     
       

def run():
    
    port = int(random.random()*1000)
    print('starting server, port', port)

    # Server settings
    server_address = ('', port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()