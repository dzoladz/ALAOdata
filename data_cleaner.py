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
import re


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

def clean_city(items):
    cities = []
    for item in items:
        if type(item) is not str:
            item = ''
            cities.append(item)
        else:
            item = str(item).lower()
            item = item.title()
            cities.append(item)
    x = pd.Series(cities)
    return x

def clean_orgs(orgs):
    organizations = []
    special_org_map = {
        "Ohionet": "OhioNET",
        "Ohiolink": "OhioLINK",
        'Oclc': 'OCLC'
    }
    for org in orgs:
        if type(org) is not str:
            org = ''
        else:
            org = str(org).title()
            for key, value in special_org_map.items():
                if org == key:
                    org = value
        organizations.append(org)
    x = pd.Series(organizations)
    return x

def clean_states(states):
    clean_states = []
    for state in states:
        if type(state) is not str:
            state = ''
        else:
            state = str(state)[:2].upper()
        clean_states.append(state)
    x = pd.Series(clean_states)
    return x

def clean_zips(zips):
    zips_list = []
    for zip in zips:
        if type(zip) is not str:
            zip = ''
        elif len(str(zip).strip()) <= 4:
            print(zip)
            zip = ''
        elif ' ' in zip:
            zip = ''
        else:
            zip = zip[:5]
        zips_list.append(zip)
    x = pd.Series(zips_list)
    return x


# MAIN PROGRAM

def main():
    # get the data
    data = grab_df()


    # do stuff with the data
    data['First name'] = data['First name'].str.title()
    data['Details to show'] = ''
    data['Work City'] = clean_city(data['Work City'])
    data['Organization'] = clean_orgs(data['Organization'])
    data['Work Province/State'] = clean_states(data['Work Province/State'])
    data['Work Postal Code'] = clean_zips(data['Work Postal Code'])


    # write the data back to file
    write_output_file(data)

if __name__ == "__main__":
    main()
