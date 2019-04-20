# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:31:19 2018

@author: white
"""
import re
import datetime

class ConvertUtil:
    def __init__(self):
        self.main_pattern="([\-0-9\.][\-0-9\.]*|[eE][eE]*|万|亿|百万|千万)"
        #        sub_pattern="([0-9\.][0-9\.]*)"
    def RegParise(self, _str):

        main_result =re.findall(self.main_pattern, _str)

        value = float(0.0)
        sign=1
        exp=0
        for x in main_result:
            if(value ==0):
                value = float(x)
                if(int(value) != 0):
                    sign = int( value/abs(value))
            elif(x == 'e' or x == 'E'):
                exp=1
            elif(x == '万'):
                value = 10000*value
                exp=0
            elif(x == '百万'):
                value = 100* 10000*value
                exp=0
            elif(x == '千万'):
                value = 1000* 10000*value
                exp=0
            elif(x == '亿'):
                value = 10000*10000*value
                exp=0
            else:
                if(exp==1):
                    value = value*pow(10, int(x))
                else:
                    value = 1000*value +sign*float(x)
                exp=0
        return value
    def StrToInt(self, _str):
        v = self.RegParise(_str)
        return int(v)

    def StrToFloat(self, _str):
        sign = 1
        if( _str[0] == '(' and _str[len(a)-1] == ')' ):
            sign = -1
        v = self.RegParise(_str)
        return sign*float(v)

    def StrToDate(self, _str):
        v = _str.replace('/','').replace('-','')
        return datetime.datetime.strptime(v,'%Y%m%d')

    def ShowNum(self, v):
        if(abs(v) >= 1000):
            print(format(v,','))
        else:
            print(v)