# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:01:00 UTC 2019

@author: white
"""
import xlwt
import csv

class csvapi(object):
    def __init__(self):
        self.__csv_file=''

    def write():
        #csv 写入
        stu1 = ['marry',26]
        stu2 = ['bob',23]
        #打开文件，追加a
        out = open('Stu_csv.csv','a', newline='')
        #设定写入模式
        csv_write = csv.writer(out,dialect='excel')
        #写入具体内容
        csv_write.writerow(stu1)
        csv_write.writerow(stu2)
        print ("write over")

    def read():
        csv_file =  csv.reader(open('Stu_csv.csv', 'r'))
        print(csv_file)
        for stu in  csv_file:
            print(type(stu), stu)
