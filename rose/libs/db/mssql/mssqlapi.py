# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:30:41 2018

@author: white
"""

import pymssql
#import datetime as dt
import numpy as np
# server 数据库服务器名称或IP
# user 用户名
# password 密码
# database 数据库名称
class mssqlapi:
    ##两个下划线开头，声明该属性为私有
    __server = ''
    __database = ''
    __user = ''
    __passwd= ''
    def __init__(self, server, database, user, passwd):
        self.__server =  server
        self.__database = database
        self.__user = user
        self.__passwd = passwd

    def __connect(self, timeout):
        try:
            #create sql connection
            self.conn = pymssql.connect(host=self.__server, database = self.__database,
                           user = self.__user, password = self.__passwd, login_timeout = timeout)
            cur = self.conn.cursor()
        except IndexError as e:
            print(e)  # string index out of range
        except IOError as e:
            print(e)
        except Exception as err:
            print( "Error decoding config file: %s" %( str(err)))
            sys.exit(1)
        else:
            print('no Error')  # 当没有错误的时候才执行
        finally:  # 不管出不出错一定会执行
            print('over')
            return cur
    def get_table(self, cmd, timeout=30):
        cursor = self.__connect(timeout)
        # 执行操作
        cursor.execute(cmd)

        #row = cursor.fetchall()
        row = cursor.fetchall()
        rowcount = cursor.rowcount
        #while row:
        #print(row) #"ID=%s, Name=%s" % (row[0], row[1]))
        #print(row)
        #row = cursor.fetchone()
        #print(row.count)

        # 也可以使用for循环来迭代查询结果
        # row = cursor.fetchone()
        # for row in cursor:
        # print("ID=%d, Name=%s" % (row[0], row[1]))
        #for row in cursor:
        #    print("ID=%s, Name=%s" % (row[0], row[1]))
        # 关闭连接
        self.conn.close()
        return rowcount,row
    def insert_data(self, cmd, timeout=30):
        print(cmd)
        cursor = self.__Connect(timeout)
        # 执行操作
        cursor.execute(cmd)

        self.conn.commit()

        self.conn.close()


    def exec_proc(self, cmd, timeout=30):
        cursor = self.__Connect(timeout)
        # 执行操作
        cursor.execute(cmd)

        #row = cursor.fetchall()
        cursor.fetchall()
        self.conn.close()


