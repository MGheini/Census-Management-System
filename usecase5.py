import xlrd
import operator
__author__ = 'M'
# -*- coding: utf-8 -*-

static_start_country = 29

def process_data(path,year):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)

    # get the first worksheet
    first_sheet = book.sheet_by_index(0)

    j=0
    for row_value in first_sheet.row_values(16):
        j += 1
        #print(row_value)
        if row_value == year:
            #print("I find it:  "+str(j))
            break

    j -= 1
    estimates = first_sheet.col_values(j)
    countries = first_sheet.col_values(2)

    dictionary = dict(zip(countries,estimates))

    print(dictionary)
    deleted_items=[]

    for item in dictionary:
        if isinstance(dictionary[item], str):
            deleted_items.append(item)
    for item in deleted_items:
        dictionary.pop(item,None)
    sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1))

    print(sorted_x)








year = input("Please enter year:")
process_data("Data/WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.XLS",year)