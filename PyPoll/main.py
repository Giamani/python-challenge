import os
import csv
from collections import Counter

# Defineing the path to the CSV file in the Resources folder
current_directory = os.path.dirname(__file__)

input_file = os.path.join(current_directory, "Resources", "election_data.csv")

# Print the current working directory to help diagnose the issue
print(f"Current Working Directory: {current_directory}")

# Initializing variables to store data
total_votes = 0
candidates = []
votes_per_candidate = Counter()

# Reading the CSV file
try:
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Going through each row in the CSV
        for row in reader:
            # Counting the total number of votes
            total_votes += 1
            
            # Storing the candidate for each vote
            candidate = row["Candidate"]
            candidates.append(candidate)
            
            # Counting the votes for each candidate
            votes_per_candidate[candidate] += 1
except FileNotFoundError:
    print(f"Error: The file {input_file} was not found.")

# Analyzing the data and finding the winner
candidate_list = list(set(candidates))
percentage_per_candidate = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_per_candidate.items()}
winner = max(votes_per_candidate, key=votes_per_candidate.get)

# Printing the election results in the terminal
print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)
for candidate in candidate_list:
    print(f"{candidate}: {percentage_per_candidate[candidate]:.3f}% ({votes_per_candidate[candidate]})")
print("-" * 30)
print(f"Winner: {winner}")
print("-" * 30)

# Exporting the election results to a text file
output_file = os.path.join(current_directory, "election_results.txt")
with open(output_file, 'w') as outfile:
    outfile.write("Election Results\n")
    outfile.write("-" * 30 + "\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-" * 30 + "\n")
    for candidate in candidate_list:
        outfile.write(f"{candidate}: {percentage_per_candidate[candidate]:.3f}% ({votes_per_candidate[candidate]})\n")
    outfile.write("-" * 30 + "\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-" * 30 + "\n")
