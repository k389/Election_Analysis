# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Traker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes +=1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count. 
        candidate_votes[candidate_name] +=1

    # Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)

    # 3. Print the total votes
    #print(total_votes)

    # Print the candidate list
    #print(candidate_options)

    # Print the candidate vote dictionary.
    #print(candidate_votes)

    # Determine the percentage of the votes for each candidate by looping through the counts
    # 1. Iterate throught the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
            # 4. Print the candidate name and percentage of votes
            #print(f"{candidate}: received {vote_percentage:.2f}% of the vote.") 

            # To do: print out each candidate's name, vote count, and percentage of # votes to the terminal
            #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # print each candidate, their vote count, and the percentage to the terminal
        print(candidate_results)
        # Save the candidate results to the text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine of the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
        
    # Print the winning candidate's results to the terminal
    winning_candidate_summary = (
        f"------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

        



    
