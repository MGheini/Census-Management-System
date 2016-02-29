import xlrd

import matplotlib.pyplot as plt


def open_file(male_path,female_path,country_name):
    """
    Open and read an Excel file
    """
    years = []
    male_population = []
    female_population = []

    book = xlrd.open_workbook(male_path)
    first_sheet = book.sheet_by_index(0)

    i = 0
    for row_value in first_sheet.col_values(2):
        i += 1
        if row_value == country_name:
            break

    j = 5
    while j < 71:
    	years.append(first_sheet.cell(16,j).value)
    	male_population.append(first_sheet.cell(i - 1,j).value)
    	j += 1

    book = xlrd.open_workbook(female_path)
    first_sheet = book.sheet_by_index(0)

    i=0
    for row_value in first_sheet.col_values(2):
        i += 1
        if row_value == country_name:
            break

    j = 5
    while j < 71:
    	female_population.append(first_sheet.cell(i - 1,j).value)
    	j += 1

    data = {}
    data['years'] = years
    data['male_population'] = male_population
    data['female_population'] = female_population

    return data


country_name = input("Please enter country name: ")

data = open_file("Data/WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.XLS", "Data/WPP2015_POP_F01_3_TOTAL_POPULATION_FEMALE.XLS", country_name)

plt.plot(data['years'], data['male_population'], '-o', label='Male')
plt.plot(data['years'], data['female_population'], '-o', color='red', label='Female')
plt.legend(loc='lower right')
plt.show()
