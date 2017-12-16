#-*- encoding=UTF-8 -*-  
__author__ = 'fyby'  
from Tkinter import *  
class App:  
    def __init__(self, master):  
        #构造函数里传入一个父组件(master),创建一个Frame组件并显示  
        frame = Frame(master) 
        master.geometry('400x200')
        frame.pack()  
        #创建两个button，并作为frame的一部分  
        self.urlpLabel= Label(frame,text="url")
        self.urlpLabel.grid(row=0,column=0)        
        self.urltext = Text(frame,width=20,height=1)
        self.urltext.grid(row=0,column=1)
        
        self.sf = Label(frame,text="Software")
        self.sf.grid(row=1,column=0)
        self.sftext= Text(frame,width=20,height=1)
        self.sftext.grid(row=1,column=1)
        
        self.button = Button(frame, text="Start", fg="red", command=self.start)  
        self.button.grid(row=3,column=0) #此处side为LEFT表示将其放置 到frame剩余空间的最左方 
        
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)  
        self.hi_there.grid(row=3,column=1)  
  
    def start(self):
        print "start"
        
    def say_hi(self):  
        print "hi there, this is a class example!"  
  
win = Tk()  
app = App(win) 
win.mainloop()