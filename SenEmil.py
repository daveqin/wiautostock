# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:55:50 2017

@author: Administrator
"""

import smtplib

from email.mime.text import MIMEText




def send_email(from_addr, to_addr, subject, password,txtMim):
    msg = MIMEText(txtMim,'html','utf-8')
    msg['From'] = u'<%s>' % from_addr
    msg['To'] = u'<%s>' % to_addr
    msg['Subject'] = subject

    smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
    smtp.set_debuglevel(1)
    smtp.ehlo("smtp.163.com")
    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, [to_addr], msg.as_string())


def SenEmails(subject,txtMim):
    # 这里的密码是开启smtp服务时输入的客户端登录授权码，并不是邮箱密码
    # 现在很多邮箱都需要先开启smtp才能这样发送邮件
    sen_emUser = u"13508767983@163.com"
    sen_passwor= u"qzf15331412185"
    to_emUser  = u"1029329095@qq.com"
    subject    = subject
    txtMim     = txtMim
    send_email(sen_emUser,to_emUser,subject,sen_passwor,txtMim)