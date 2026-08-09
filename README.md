# MoodleAnonymizer
***Created by Dulith Polpitiya***

This program, ``anonymizer.py``, receives Moodle log files as an input and anonymizes them to respect the privacy of the students and instructors.

## How to run anonymizer.py

1. Run the file in your preferred Python interpreter.
2. Enter the name of the log file. *Note that the file must be a .csv file: you can also just type the name of the file without including the file extension.*
3. Enter your desired name for the anonymized file.
4. Enter the name of the column where the users' names and registration numbers appear. *(In your case, it will most likely be **User full name**)*
5. Enter the name of the column where the affected users' names and registration numbers appear. *(In your case, it will most likely be **Affected user**)*

If you possess a results file, you may anonymize this file as well. **Note that the results file must be a .csv file.**

6. Enter the name of the results file.
7. Enter the name of the column where the users' registration numbers appear. *(In your case, it will most likely be **Reg. No.**)*
