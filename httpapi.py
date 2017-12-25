# coding:utf-8

import json
from urlparse import parse_qs
from wsgiref.simple_server import make_server
from stockapi import *



        
        

# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'text/html')])
    # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
    # 获取当前get请求的所有数据，返回是string类型
    params = parse_qs(environ['QUERY_STRING'])
    # 获取get中key为name的值
    name = params.get('name', [''])[0]
    no = params.get('no', [''])[0]
    
    action = params.get('action', [''])[0]
    stock = params.get('stock', [''])[0]
    
    jsoncallback= params.get('jsoncallback', [''])[0]
    #print callbacks
    
    if action=='get_hist':
         
          #print get_hist(stock)
          dic=get_hist(stock)
          
          #dic= {'callbacks': callbacks,'action':action}
          return jsoncallback+"("+dic+")"
    
    # 组成一个数组，数组中只有一个字典
    dic = {'name': name, 'no': no,'action':action}
    
    #$_GET['jsoncallback'] . "(".json_encode($array_e).")";
    print "xxx("+json.dumps(dic)+")"
    return jsoncallback+"("+json.dumps(dic)+")"


if __name__ == "__main__":
   port = 6276
   httpd = make_server("0.0.0.0", port, application)
   print "serving http on port {0}...".format(str(port))
   httpd.serve_forever()
 
#print get_hist('002486')