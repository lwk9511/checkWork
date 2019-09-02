#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd

# locPath='G:\\车管家项目资料\\'
locPath='E:\\考勤\\杭走临安\\'

def read_excel(path):
    truncatefile(path)
    # 打开文件
    workbook = xlrd.open_workbook(locPath+'2019-8月考勤报表.xlsx')
    # 获取所有sheet
    sheet_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_index(0)  # sheet索引从0开始
    # sheet = workbook.sheet_by_name('Sheet1')

    # print (workboot.sheets()[0])
    # sheet的名称，行数，列数
    print(sheet.name, sheet.nrows, sheet.ncols)

    # 获取整行和整列的值（数组）
    rows = sheet.row_values(1)  # 获取第2行内容
    # cols = sheet.col_values(2) # 获取第3列内容
    # print (cols)
    for rown in range(sheet.nrows):
        if sheet.cell_value(rown, 7)!='' and sheet.cell_value(rown, 7)!= None:
            content=sheet.cell_value(rown, 1)+","+sheet.cell_value(rown, 3)+","+sheet.cell_value(rown, 7)
            write(path,content)

# 写入文档
def write(path, text):
    with open(path, 'a', encoding='utf-8') as f:
        f.writelines(text)
        f.write('\n')
# 清空文档
def truncatefile(path):
    with open(path, 'w', encoding='utf-8') as f:
        f.truncate()

# -------------------------------------------------------启动-----------------------------------------------------------
if __name__ == '__main__':
    path = locPath+'考勤数据.txt'
    read_excel(path)

