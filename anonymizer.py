"""
Moodle Log Anonymizer
Created by Dulith Polpitiya
June 30, 2026

This program receives Moodle log files as an input
and anonymizes them to respect the privacy of
the students and instructors.
"""

import numpy as np
import pandas as pd

# df = pd.read_csv('logs_CO1010-2024-E23_20251020-0110.csv')
# df_marks = pd.read_csv('CO1010_E23_Marks_All.csv')

try:
    # input file name
    input_name = input("Enter input file name: ")
    if not input_name.endswith(".csv"): # if user forgets to add .csv
        input_name = f"{input_name}.csv"
    df = pd.read_csv(input_name)

    # output file name
    output_name = input("Enter output file name: ")
    if not output_name.endswith(".csv"):
        output_name = f"{output_name}.csv" # if user forgets to add .csv

    # additional info
    user_id = input("What is the name of the column where the user's name and registration number are found: ")
    affected_user = input("What is the name of the column where the affected user's name and registration number are found: ")

    # remove ip address column
    try:
        df = df.drop(columns='IP address')
    except Exception:
        pass

    # drop empty cells
    df[affected_user] = df[affected_user].replace('-', np.nan)

    # extract registration numbers
    # for users with no reg. no., extract their names instead
    reg_ids = df[user_id].str.extract(r'(E/\d{2}/\d{3})')[0].fillna(df[user_id])
    reg_ids_2 = df[affected_user].str.extract(r'(E/\d{2}/\d{3})')[0].fillna(df[affected_user])

    # get unique ids
    unique_reg_ids = pd.concat([reg_ids, reg_ids_2]).dropna().unique()

    # create a dictionary mapping all users onto an anonymous pseudonym (User1, User2, etc.)
    user_map = {reg_id: f"User{i + 1}" for i, reg_id in enumerate(unique_reg_ids)}

    # save dictionary to csv file
    pd.DataFrame(user_map, index=[0]).to_csv(f'user_map_{output_name}', index=True)

    # map onto columns
    df[user_id] = reg_ids.map(user_map)
    df[affected_user] = reg_ids_2.map(user_map)
    df = df.rename(columns={user_id: 'user_id'})  # rename column

    # save new csv
    df.to_csv(output_name, index=False)

    # map onto marks list
    answer = input("Do you also posses a results file, and would you like for this file to be anonymized? (Y/N): ")
    if answer == 'Y' or answer == 'y':
        # input file name
        input_name = input("Enter results file name: ")
        if not input_name.endswith(".csv"): # if user forgets to add .csv
            input_name = f"{input_name}.csv"
        df_marks = pd.read_csv(input_name)

        # additional info
        reg_no = input("What is the name of the column where the registration numbers are found: ")

        reg_ids_3 = df_marks[reg_no]
        df_marks[reg_no] = reg_ids_3.map(user_map)
        df_marks = df_marks.rename(columns={reg_no: 'user_id'}) # rename column

        # save to new csv
        df_marks.to_csv(f'marks_{output_name}', index=False)

except FileNotFoundError:
    print("\033[31mFile not found.\033[31m")
except Exception as e:
    print("\033[31mAn error occurred. You most likely entered a column name incorrectly.\033[31m")