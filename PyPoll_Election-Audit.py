##### Election Audit #######
# Add dependencies.
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
# Initizialize variables to track winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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


# Print the candidates' votes
# print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts
# Iterate throught the candidate list
for candidate_name in candidate_votes:
    # retrieve a candidate's vote count
    votes = candidate_votes[candidate_name]
    # convert to floats and calculate percentage
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print each candidate's name, vote count, and percentage of votes to terminal
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # and set winning_candidate to candidat's name
        winning_candidate = candidate_name
    
# Print the winning candidate's name, vote count and percentage
winning_candidate_summary = (
    f'-------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
)
print(winning_candidate_summary)