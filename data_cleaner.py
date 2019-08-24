#!/usr/local/bin/python3
# Authors: Derek Zoladz & Ryan Scott
#
# Description: Data clean-up for the Academic Library Association of Ohio (ALAO)
# Notes: Output files will be in .csv format
#
###############################################
# SET SCRIPT VARIABLES
input_filename = 'ALAOdata.csv'
output_filename = 'ALAOdata-clean.csv'

###############################################

# IMPORT STATEMENTS
import pandas as pd
import os


# FUNCTION DEFINITIONS

def grab_df():
    cd = os.getcwd()
    input_file = cd + '/' + input_filename
    df = pd.read_csv(input_file)
    return df

def write_output_file(df):
    cd = os.getcwd()
    output_file = cd + '/' + output_filename
    df.to_csv(output_file, encoding='utf-8')

def city(items):
    cities = []
    for item in items:
        if type(item) is not str:
            item = ''
            cities.append(item)
        else:
            item = str(item).lower()
            item = item.title()
            cities.append(item)
    a = pd.Series(cities)
    return a


# MAIN PROGRAM

def main():
    # get the data
    data = grab_df()


    # do stuff with the data
    data['First name'] = data['First name'].str.title()
    data['Details to show'] = ''
    data['Work City'] = city(data['Work City'])


    # write the data back to file
    write_output_file(data)

if __name__ == "__main__":
    main()
