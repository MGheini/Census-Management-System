__author__ = 'M'
# -*- coding: utf-8 -*-



def secure_country(country):
    with open("secured_countries.txt", "a") as myfile:
        myfile.write(country+"\n")

country = input("Please enter country name:")
secure_country(country)