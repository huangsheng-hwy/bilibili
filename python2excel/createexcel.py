import xlwings

excelApp = xlwings.App(False, False)
excelFile = excelApp.books.add()


# 创建excel表格
def createExcel(excel_name):
    excelFile.save(excel_name)


# 给excel表格增加sheet
def addSheet(excel_name):
    excelFile.sheets.add("test")
    excelFile.save("1.xlsx")


if __name__ == '__main__':
    excel_name = "1.xlsx"
    createExcel(excel_name)
    addSheet(excel_name)
