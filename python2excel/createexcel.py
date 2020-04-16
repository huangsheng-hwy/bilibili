import xlwings




# 创建excel表格
def createExcel(excel_name):
    excelApp = xlwings.App(False, False)
    excelFile = excelApp.books.add()
    excelFile.save(excel_name)
    excelFile.close()
    excelApp.quit()



# 给excel表格增加sheet
def addSheet(excel_name):
    excelApp = xlwings.App(False, False)
    excelFile = excelApp.books.add()
    excelFile.sheets.add("test")
    excelFile.save("1.xlsx")


if __name__ == '__main__':
    for i in range(0,4):
        excel_name = "d:\\test\\{}.xlsx".format(i)
        createExcel(excel_name)

    # addSheet(excel_name)
