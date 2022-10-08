import pandas as pd
import os

# merge numerous workbooks into single workbook
def mergeWorkbooks():
    dataList = [] # store files in a list
    for fileName in os.listdir("."):
        # find the target files
        if fileName.startswith("20") and fileName.endswith(".xlsx"):
            dataList.append(pd.read_excel(fileName))


    dataAll = pd.concat(dataList) # combine data
    combinedFileName = "2017 - 2021.xlsx" # name of the combined file
    dataAll.to_excel(combinedFileName, index=False) # export to an Excel file


# merge numerous "worksheets" in a workbook
import xlwings as xw
def mergeWorkSheets():
    dataList = pd.read_excel("2017 - 2021.xlsx", sheet_name=None)
    dataAll = pd.concat(dataList.values())

    app = xw.App(visible=False, add_book=False)
    workbook = app.books.open("2017 - 2021.xlsx")
    workbook.sheets.add("Summary", before=workbook.sheets[0]) # add a worksheet on top which combines all info in other sheets
    workbook.sheets["Summary"].range("A1").options(index=False).value = dataAll # copy data to the first sheet

    workbook.save()
    workbook.close()

    app.quit()







