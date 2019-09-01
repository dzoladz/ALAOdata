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
            zip = ''
        elif ' ' in zip:
            zip = ''
        else:
            zip = zip[:5]
        zips_list.append(zip)
    x = pd.Series(zips_list)
    return x

def clean_phone(numbers):
    clean_numbers = []
    for number in numbers:
        if type(number) is not str:
            number = ''
        else:
            number = re.sub('[^0-9]', '', number)
            # NANP rules do not permit the digits 0 and 1 as the leading digit
            if number.startswith('0') or len(number) < 7:
                number = ''
            elif number.startswith('1'):
                number = re.sub('^([1]{1})([0-9]{3})([0-9]{3})([0-9]{4})', '1-\\2-\\3-\\4', number)
            elif len(number) == 7:
                number = re.sub('^([0-9]{3})([0-9]{4})', '\\1-\\2', number)
            elif len(number) == 10:
                number = re.sub('^([0-9]{3})([0-9]{3})([0-9]{4})', '\\1-\\2-\\3', number)
            elif len(number) > 10:
                number = re.sub('^([0-9]{3})([0-9]{3})([0-9]{4})([0-9])', '\\1-\\2-\\3 x\\4', number)
            else:
                number = ''
        clean_numbers.append(number)
    x = pd.Series(clean_numbers)
    return x

# MAIN PROGRAM

def main():
    # get the data
    data = grab_df()

    # drop these columns
    drop_columns = [
        'Password',
        'Interest Groups',
        'ACRL Member',
        'Membership History (2010 & prior)',
        'Retired',
        'Group participation',
        'Current Leadership Positions',
        'Past Leadership Positions',
        'Current Committees',
        'Past Committees',
        'ALAO Awards',
        'Directory listing text',
        'Expected Graduation Date',
        'School Attending',
        'Archived',
        'Subscribed to emails',
        'Subscription source',
        'Opted in',
        'Event announcements',
        'Member emails and newsletters',
        'Administration access',
        'Created on',
        'Profile last updated',
        'Last login',
        'Updated by',
        'Balance',
        'Total donated',
        'Membership enabled',
        'Membership level',
        'Membership status',
        'Member since',
        'Renewal due',
        'Renewal date last changed',
        'Level last changed',
        'Access to profile by others',
        'Details to show',
        'Photo albums enabled',
        'Member bundle ID or email',
        'Member role',
        'Details to show'
    ]
    data.drop(drop_columns, inplace=True, axis=1)


    # do stuff with the data
    data['First name'] = data['First name'].str.title()
    data['Work City'] = clean_city(data['Work City'])
    data['Organization'] = clean_orgs(data['Organization'])
    data['Work Province/State'] = clean_states(data['Work Province/State'])
    data['Work Postal Code'] = clean_zips(data['Work Postal Code'])
    data['Preferred Phone'] = clean_phone(data['Preferred Phone'])
    data['Work Phone'] = clean_phone(data['Work Phone'])
    data['Work Cellular Phone'] = clean_phone(data['Work Cellular Phone'])
    data['Work Fax Number'] = clean_phone(data['Work Fax Number'])
    data['Home Phone'] = clean_phone(data['Home Phone'])
    data['Home Cellular Phone'] = clean_phone(data['Home Cellular Phone'])
    data['Home Fax Number'] = clean_phone(data['Home Fax Number'])


    # write the data back to file
    write_output_file(data)

if __name__ == "__main__":
    main()
