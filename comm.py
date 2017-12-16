# -*- coding: gb2312 -*- 
'''
公共函数

'''


def writTxt(fileName,data):
    txt = open(fileName,'a')
    txt.write(data)
    txt.write('\n')
    txt.close()
    
#字符转换
def gbk2utf8(s):  
    return s.decode('gbk').encode('utf-8')

