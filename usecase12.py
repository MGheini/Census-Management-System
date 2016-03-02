import xlrd

import matplotlib.pyplot as plt


def open_file(male_path,female_path,year_number):
    """
    Open and read an Excel file
    """

    male_population = []
    female_population = []

    book = xlrd.open_workbook(male_path)
    first_sheet = book.sheet_by_index(0)

    row = first_sheet.row(16);
    i = 0
    for cell in row:
        i += 1
        if cell.value == year_number:
            break

    j = 17
    while j < 258:
    	male_population.append(first_sheet.cell(j,i - 1).value)
    	j += 1

    book = xlrd.open_workbook(female_path)
    first_sheet = book.sheet_by_index(0)

    row = first_sheet.row(16);
    i=0
    for cell in row:
        i += 1
        if cell.value == year_number:
            break

    j = 17
    while j < 258:
    	female_population.append(first_sheet.cell(j,i - 1).value)
    	j += 1

    data = {}
    data['male_population'] = male_population
    data['female_population'] = female_population

    return data


year_number = input("Please enter the year number: ")

data = open_file("Data/WPP2015_POP_F01_2_TOTAL_POPULATION_MALE.XLS", "Data/WPP2015_POP_F01_3_TOTAL_POPULATION_FEMALE.XLS", year_number)

plt.boxplot([data['male_population'], data['female_population']])
plt.xticks([1, 2], ['male', 'female'])
plt.show()
