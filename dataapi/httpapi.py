# coding:utf-8

import json
from urlparse import parse_qs
from wsgiref.simple_server import make_server
from stockapi import stockapi
import random
#获取请的参数
def get_params(params):
    

    stock       = params.get('stock', [''])[0]
    
    action      = params.get('action', [''])[0]
    jsoncallback= params.get('jsoncallback', [''])[0]
    #生成字典
   
    params_arr  = {'stock':stock,'action':action,'jsoncallback':jsoncallback}
    
    return params_arr
#对请进行操作        
def do_action(action,stock):
   
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

# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'text/html')])
    # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
    # 获取当前get请求的所有数据，返回是string类型
    params     = parse_qs(environ['QUERY_STRING'])
    params_arr = get_params(params)
    
    stock       = params_arr['stock']
    action      = params_arr['action']
    jsoncallback= params_arr['jsoncallback']
    data =do_action(action,stock)
    
    
    return jsoncallback+"("+data+")"
    #///////////////////////////////
    
 
    # 获取get中key为name的值
    


    # 组成一个数组，数组中只有一个字典
    #dic = {'name': name, 'no': no,'action':action}
    
    #$_GET['jsoncallback'] . "(".json_encode($array_e).")";
    #print "xxx("+json.dumps(dic)+")"
    #return jsoncallback+"("+json.dumps(dic)+")"


if __name__ == "__main__":
   port = int(random.random()*1000)
   httpd = make_server("0.0.0.0", port, application)
   print ("serving http on port {0}...".format(str(port)))
   httpd.serve_forever()
 
#print get_hist('002486')