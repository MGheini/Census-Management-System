import xlrd

__author__ = 'M'
# -*- coding: utf-8 -*-


def process_data(path , country_name , year):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)

    # get the first worksheet
    first_sheet = book.sheet_by_index(0)
    i=0
    for row_value in first_sheet.col_values(2):
        i += 1
        #print(row_value)
        if row_value == country_name:
            #print("I find it:  "+str(i))
            break

    j=0
    for row_value in first_sheet.row_values(16):
        j += 1
        #print(row_value)
        if row_value == year:
            #print("I find it:  "+str(j))
            break


    # read a cell
    cell = first_sheet.cell(i-1,j-1)
    print(cell.value)




country_name = input("Please enter country name:")
year = input("Please enter year:")

process_data("Data/WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.XLS",country_name,year)


