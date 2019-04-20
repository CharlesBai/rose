#!/usr/bin/python
#coding: utf-8

import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
#import numpy as np
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

class mail_model:
    __smtpserver=''
    __user=''
    __psword=''
    __att_name = False
    def __init__(self, smtpserver,user,psword):
        #1. 设置邮箱发送服务器
        self.__smtpserver = smtpserver        
        #2. 设置发件人及密码
        self.__user = user
        self.__psword=psword

    def set_subject(self, newSubject):
        self.subject = newSubject

    def set_text(self, newText):
        self.text = newText

    def set_receiver(self, newReceiver, newCC=None):
        self.to = newReceiver
        self.cc = None if newCC==None else newCC

    def set_attach(self, newAtt_name):
        self.att_name = newAtt_name
    def mail_init(self):
        #1. 设置发件人及密码
        self.sender =  self.__user

        #2. 注册邮箱, 设置邮箱内容及添加附件
        if self.__att_name != False :
            print('now with attach')
            self.msg = MIMEMultipart('mixed')

            #2.1. 设置邮件内容
            text_plain = MIMEText(self.text,'plain', 'utf-8')
            self.msg.attach(text_plain)

            #2.2. 设置附件
            sendfile=open(self.__att_name,'rb').read()
            text_att = MIMEText(sendfile, 'base64', 'utf-8')
            text_att["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            # text_att["Content-Disposition"] = 'attachment; filename="test.txt"'
            text_att["Content-Disposition"] = 'attachment; filename="%s"'%(self.__att_name)
            print(text_att["Content-Disposition"])

            self.msg.attach(text_att)
        else:
            #2.1. 设置邮件内容
            print('now without attach')
            self.msg = MIMEText(self.text, 'plain', 'utf-8')

        #3. 设置邮箱标题
        #解决中文标题为乱码的问题
        # if not isinstance(self.subject,unicode):
        #    self.subject = unicode(self.subject)
        self.msg['Subject'] = self.subject
        #4. 设置发件人
        # self.msg['From'] = 'charlesbai@pantek-cn.com <charlesbai@pantek-cn.com>'
        self.msg['From'] = self.__user;
        #self.msg['Accept-Charset'] = 'ISO-8859-1,utf-8'
        #5. 设置收件人
#        self.msg['To'] =  self.username
        #收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
        self.msg['To'] = ";".join(self.to)
        if(self.cc != None):
            self.msg['Cc'] = ";".join(self.cc)

        if(self.cc != None):
            self.receiver = np.concatenate([self.to, self.cc])
        else:
            self.receiver = np.concatenate([self.to])
    def show_mail(self):
        print(self.msg['Subject'])
        print(self.msg['From'])
        print(self.msg['To'])
        print(self.msg['Cc'])
        print(self.receiver)

    def send_mail(self):

        #发送邮件
        try:
            smtp = smtplib.SMTP(self.smtpserver, 587)
            #smtp = smtplib.SMTP(self.smtpserver, 25)
            #我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
            #smtp.set_debuglevel(1)
            smtp.login(self.__user, self.__psword)
            result = smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
            smtp.quit()
            smtp.close()
            print("邮件发送成功 %s "%(result))
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")