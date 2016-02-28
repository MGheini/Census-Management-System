import xlrd
import operator
__author__ = 'M'
# -*- coding: utf-8 -*-

static_start_country = 29

def open_file(path, year , variant):
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

    j=0
    found = False
    for row_value in sheet.row_values(16):
        j += 1
        #print(row_value)
        if row_value == year:
            #print("I find it:  "+str(j))
            found = True
            break
    if found == False :
        print("data for this year is not available!")
        return


    j -= 1
    values = sheet.col_values(j)
    countries = sheet.col_values(2)

    dictionary = dict(zip(countries,values))

    deleted_items=[]

    for item in dictionary:
        if isinstance(dictionary[item], str):
            deleted_items.append(item)
    for item in deleted_items:
        dictionary.pop(item,None)
    sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1))

    print(sorted_x)


year = input("Please enter year:")
variant = input("Please enter variant:")
open_file("Data/WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.XLS",year,variant)