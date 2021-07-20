# Import the datetime class from the datetime module.
import datetime

# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

# Open and read file
with open(file_to_load) as election_data:

    # To do: Perform analysis
    print(election_data)

# Write to file: Create filename variable
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")