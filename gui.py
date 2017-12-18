# -*- coding: gb2312 -*-

__author__ = 'fyby'  
from Tkinter import *  
from winautos import *
import win32gui, win32api, win32con
from comm import *
from httpServ import start_server
import threading

class App:  
    def __init__(self, master):  
        #构造函数里传入一个父组件(master),创建一个Frame组件并显示  
        frame = Frame(master) 
        master.geometry('400x200')
        frame.pack()  
        #创建两个button，并作为frame的一部分  
        self.urlpLabel= Label(frame,text=u"软件位置")
        self.urlpLabel.grid(row=0,column=0)  
        sf_text = StringVar()        
        self.sf = Entry(frame, textvariable = sf_text)
        sf_text.set(u"输入软件位置")
        self.sf.grid(row=0,column=1)
        ps_text = StringVar()  
        self.pstext = Entry(frame,textvariable = ps_text)
        ps_text.set(u"输入密码")
        self.pstext.grid(row=0,column=2)
        
        
        
        self.sftime = Label(frame,text=u"启动时间")
        self.sftime.grid(row=1,column=0)
        tt = StringVar() 
        self.sfttext= Entry(frame,textvariable = tt)
        tt.set(u"24:24")
        self.sfttext.grid(row=1,column=1)
        self.hobby1 = BooleanVar()  
        self.checkb1 = Checkbutton(frame,text = u"启动",variable = self.hobby1)  
        self.checkb1.grid(row=1,column=2)
        
        self.httplab = Label(frame,text=u"服务器启动")
        self.httplab.grid(row=2,column=0)
        htt = StringVar() 
        self.httpport= Entry(frame,textvariable = htt)
        htt.set(u"服务器端口")
        self.httpport.grid(row=2,column=1)
        self.hobby2 = BooleanVar()  
        self.checkb2 = Checkbutton(frame,text = u"启动",variable = self.hobby2)  
        self.checkb2.grid(row=2,column=2)        
        
        
        
        self.button = Button(frame, text=u"启动", fg="red", command=self.start)  
        self.button.grid(row=3,column=0) #此处side为LEFT表示将其放置 到frame剩余空间的最左方 
        
        self.hi_there = Button(frame, text=u"测试", command=self.appStart)  
        self.hi_there.grid(row=3,column=1)  
  
    def start(self):
        writTxt('r.txt',"999")
        if self.hobby1.get()==1:
            writTxt('r.txt',"hobb1")
        if self.hobby2.get()==1:
            self.startHtt()
        
    def say_hi(self):  
        print "hi there, this is a class example!" 
        
    def startHtt(self):
        threads = []
        port = self.httpport.get()
        t1 = threading.Thread(target=start_server,args=(port,))
        threads.append(t1)
        for t in threads:
            t.setDaemon(True)
            t.start()      
        
    def appStart(self):
        
        sf=self.sf.get().encode("gb2312")
        ps=self.pstext.get().encode("gb2312")
        ver ='ver=1 "0711296a70d754483fcce2ba9c94b6e448457994449ba09ccf00ee086207cb8446b818429656b7501e7babec2ecf0328dc2fee4846e33d886d50f77a1b30dd84"'
        #win32api.ShellExecute(0, 'open',sf,ver,'',1) 
        kk = Winauto(sf,ver,ps) 
        
       
  
win = Tk()  
app = App(win) 
win.mainloop()
  
