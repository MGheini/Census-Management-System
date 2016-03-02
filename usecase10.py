import xlrd

__author__ = 'M'
# -*- coding: utf-8 -*-


def process_data(path , variant):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)

    i=0
    sheet_founded = False
    for sheet in book.sheet_names():
        i += 1
        if sheet == variant:
            sheet_founded = True
            break

    if sheet_founded == False :
        print("data for this variant is not available!")
        return
    sheet = book.sheet_by_index(i-1)

    cols_len = len(sheet.row_values(0))
    rows_len = len(sheet.col_values(0))

    for k in range(17,rows_len):
        printed = False
        for i in range(5,cols_len):
            if sheet.cell(k,i).value < 0:
                if not printed:
                    print()
                    print(sheet.cell(k,2).value)
                    printed = True
                print(sheet.cell(16,i).value)




variant = input("Please enter variant:")

process_data("Data/WPP2015_POP_F02_POPULATION_GROWTH_RATE.XLS" , variant)


