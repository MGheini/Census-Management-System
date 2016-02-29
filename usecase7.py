import xlrd

import matplotlib.pyplot as plt


def open_file(path,country_name,variant):
    """
    Open and read an Excel file
    """
    years = []
    variant_value = []

    book = xlrd.open_workbook(path)
    first_sheet = book.sheet_by_name(variant)

    i = 0
    for row_value in first_sheet.col_values(2):
        i += 1
        if row_value == country_name:
            break

    j = 5
    while j < 91:
    	years.append(first_sheet.cell(16,j).value)
    	variant_value.append(first_sheet.cell(i - 1,j).value)
    	j += 1

    data = {}
    data['years'] = years
    data['variant_value'] = variant_value

    return data


country_name = input("Please enter country name: ")
variant = input("Please enter variant: ")

data = open_file("Data/WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.XLS", country_name, variant)

plt.plot(data['years'], data['variant_value'], '-o')
plt.show()
