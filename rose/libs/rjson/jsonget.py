# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 14:40:30 2018

@author: white
"""

from urllib import parse,request

class jsonget(object):
    def __init__(self, url, param, encode):
        self.__url = url
        self.__param = param
        self.__encode = encode

    def __GetReponse(self):
    #    textmod = parse.urlencode(param)
        reqUrl="%s?%s"%(self.__url, parse.urlencode(self.__param))
        header_dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Accept-Language':'zh-CN,zh;q=0.8'
        #'Accept-Encoding':'gzip, deflate, sdch'
        }
        req = request.Request(url=reqUrl, headers=header_dict)
        res = request.urlopen(req)
        res = res.read()
        result=res.decode(encoding=self.__encode)
        return result

    def SaftyGetReponse(self,maxTime=0):
        try:
            result = self.__GetReponse()
        except :
            if (maxTime > 0):
                #递归调用次数减1
                maxTime -= 1;
                #System.Threading.Thread.Sleep(60 * 60 * 1000);
                result = self.SaftyGetJsonReponse(maxTime);
            else:
                result = None
        finally:
            return result

