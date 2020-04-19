# -*- coding: utf-8 -*-
# @Time : 2020/4/19 21:17
# @Author : python自动化办公社区
# @File : read.py
# @Software: PyCharm
# @Description:
#               1、读取excel中的所有内容
#               2、单个文件、文件夹下所有文件

import glob
import xlwings as xw

# 读取文件夹下所有的excel文档
x = glob.glob(r'D:\test\*.xls*')
# 是否有excel文档
if len(x):
    print(x)
    # 遍历excel文档
    for y in x:
        # 生成文件对象
        wb = xw.Book(y)
        # 读取指定的sheet
        sht = wb.sheets[0]
        # 读取指定的单元格
        value = sht.range('b2').value
        print(type(value))
        # print(sht.range('b2').value,'--->',sht.range('c2').value)
        wb.app.quit()
else:
    print('no related files')
