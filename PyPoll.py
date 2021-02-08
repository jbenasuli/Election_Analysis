# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of the candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

##### Import the election results csv - V1 ######
# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)
    
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as txt_file:

# # Write three counties to the file.
#     txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")

# ###### checking election analysis data #########
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Read the file object with the reader function.
#     file_reader = csv.reader(election_data)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)


# ####### check election csv headers #######
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read and print the header row.
#     headers = next(file_reader)
#     print(headers)

# ##### getting the total votes #######
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("Analysis", "election_analysis.txt")

# # 1. Initialize a total vote counter.
# total_votes = 0

# # Open the election results and read the file
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # 2. Add to the total vote count.
#         total_votes += 1

# # 3. Print the total votes.
# print(total_votes)

# ##### getting the candidates' names #######
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("Analysis", "election_analysis.txt")

# # Initialize a total vote counter
# total_votes = 0

# # Declare a new list to hold candidate options
# candidate_options = []

# # Open the election results and read the file
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row
#     headers = next(file_reader)

#     # Print each row in the CSV file
#     for row in file_reader:
#         # Add to the total vote count
#         total_votes += 1
        
#         # Print the candidate name from each row
#         candidate_name = row[2]

#         # Use if statement to return only unique values
#         if candidate_name not in candidate_options:
#             # Add the candidate name to the candidate list
#             candidate_options.append(candidate_name)

# # Print the candidate list
# print(candidate_options)

##### getting the candidates' votes #######
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Declare a new list to hold candidate options
candidate_options = []
# Declare a new dictionary to hold candidates' votes
candidate_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        # Use if statement to return only unique names
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Initialize the candidate's total vote counter
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's total count
        candidate_votes[candidate_name] += 1


# Print the candidate list
print(candidate_votes)