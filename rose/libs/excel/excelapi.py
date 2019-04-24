# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:01:00 UTC 2019

@author: white
"""
import xlwt
import xlrd
from datetime import date,datetime

class excelapi(object):
    def __init__(self):
        self.__excel_file = 'test.xls'

    #设置表格样式
    def set_style(self, name,height,bold=False):
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = name
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font
        return style

    #写Excel
    def write_excel(self):
        f = xlwt.Workbook()
        sheet1 = f.add_sheet('学生',cell_overwrite_ok=True)
        row0 = ["姓名","年龄","出生日期","爱好"]
        colum0 = ["张三","李四","恋习Python","小明","小红","无名"]
        #写第一行
        for i in range(0,len(row0)):
            sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))
        #写第一列
        for i in range(0,len(colum0)):
            sheet1.write(i+1,0,colum0[i],set_style('Times New Roman',220,True))

        sheet1.write(1,3,'2006/12/12')
        sheet1.write_merge(6,6,1,3,'未知')#合并行单元格
        sheet1.write_merge(1,2,3,3,'打游戏')#合并列单元格
        sheet1.write_merge(4,5,3,3,'打篮球')

        f.save(self.__excel_file)



    def read_excel(self):

        wb = xlrd.open_workbook(filename=self.__excel_file)#打开文件
        print(wb.sheet_names())#获取所有表格名字

        sheet1 = wb.sheet_by_index(0)#通过索引获取表格
        sheet2 = wb.sheet_by_name('学生')#通过名字获取表格
        print(sheet1,sheet2)
        print(sheet1.name,sheet1.nrows,sheet1.ncols)
        print(sheet2.name,sheet2.nrows,sheet2.ncols)

        rows = sheet1.row_values(2)#获取行内容
        cols = sheet1.col_values(3)#获取列内容
        print(rows)
        print(cols)

#if __name__ == '__main__':
#    write_excel()
