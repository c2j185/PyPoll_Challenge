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


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as text_file:
    election_counties = (
        f"\nCounties in the Election\n"
        f"-------------------------------------\n"
        f"Arapahoe\nDenver\nJefferson\n")

    # Write the text to the file.
    text_file.write(election_counties)

    # Print the data to the screen.
    print(election_counties)

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)