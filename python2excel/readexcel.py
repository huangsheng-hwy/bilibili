import os


# rootdir = 'd:\\test'
# list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
# for i in range(0,len(list)):
#        path = os.path.join(rootdir,list[i])
#        print(path)
       # if os.path.isfile(path):
       #     print()
       #     pass


# https://www.jianshu.com/p/e21894fc5501


import xlwings as xw
import pandas as pd

file = 'd:\\test\\1.xlsx'

df = pd.DataFrame([[1,2],[3,4]],
             columns=['c1','c2'],
             index=['r1','r2'])
wb = xw.Book()
sheet = wb.sheets['Sheet1']
sheet.range('A1').value = df
# sheet.range('A1').options(pd.DataFrame,expand='table').value
wb.save(path=file)
# 没有close，会出现最后一个文件打开未关闭的问题
wb.close()

