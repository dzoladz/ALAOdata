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

wa_schema = [
    #'Member ID',
    #'First name',
    'Last name',
    'Organization',
    #'Preferred Email',
    'Preferred Phone',
    #'Preferred Mail Option',
    #'Password',
    'Job title',
    'Library or Department Within Parent Organization',
    'Work Address 1',
    'Work Address 2',
    #'Work City',
    'Work Province/State',
    'Work Postal Code',
    'Work Country',
    'Work Email Address',
    'Work Phone',
    'Work Cellular Phone',
    'Work Fax Number',
    'Home Address 1',
    'Home Address 2',
    'Home City',
    'Home Province/State',
    'Home Postal Code',
    'Home Country',
    'Home Email Address',
    'Home Phone',
    'Home Cellular Phone',
    'Home Fax Number',
    'ACRL Member',
    #'Interest Groups',
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
    #'Archived',
    #'Subscribed to emails',
    #'Subscription source',
    #'Opted in',
    #'Event announcements',
    #'Member emails and newsletters',
    #'Administration access',
    #'Created on',
    #'Profile last updated',
    #'Last login',
    #'Updated by',
    #'Balance',
    #'Total donated',
    #'Membership enabled',
    #'Membership level',
    #'Membership status',
    #'Member since',
    #'Renewal due',
    #'Renewal date last changed',
    #'Level last changed',
    #'Access to profile by others',
    #'Details to show',
    #'Photo albums enabled',
    #'Member bundle ID or email',
    #'Member role'
]

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
