import xlwings as xw

# create empty workbooks to store similar data
def createNumeriousWorkBooks():
    app = xw.App(visible=False, add_book=False)
# create workbooks from 2017 - 2022
    years = list(range (2017,2022))

    for year in years:
        workbook = app.books.add()
        workbook.save(f"./{year}.xlsx")
