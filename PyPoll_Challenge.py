# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Challenge Questions
    #The voter turnout for each county
    #The number of votes that were cast from each county
    #The percentage of votes each county contributed to the election

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

#Create a list for the counties
counties_option = []

# Declare the empty dictionary for votes and counties
candidate_votes = {}
county_votes = {}

# Winning Candidate, Winning Count Traker and largest county turnout
winning_candidate = ""
winning_count = 0
winning_percentage = 0
largest_county_turnout = ""
largest_county_count = 0
largest_coounty_percentage = 0



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
        county_name = row[1]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count. 
        candidate_votes[candidate_name] +=1

        #if county does not match any counties in the data
        if county_name not in counties_option:

            #Add the county name to the counties list
            counties_option.append(county_name)

            #Track the county vote count
            county_votes[county_name] = 0

        #Add a vote to the county's count
        county_votes[county_name] +=1

    
# Save the results to the text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")

    #Save the final vote count to the text file.
    txt_file.write(election_results)

    #Print the total votes
    #print(total_votes)

    # Print the candidate list
    #print(candidate_options)

    #Print counties
    #print(counties_option)

    #print county vote dictionary
    #print(county_votes)

    # Print the candidate vote dictionary.
    #print(candidate_votes)

    #Determine the percentage of the votes for each county by looping through the counts
    #Iterate through the county list
    for county_name in county_votes:
        #retrieve vote count of a county
        votes_county = county_votes[county_name]
        #Calculate the Percentage of votes
        vote_county_percentage = int(votes_county) / int(total_votes) * 100
        #Print the county name, percentage of votes and vote county
        county_results = (f"{county_name}: {vote_county_percentage:.1f}% ({votes_county:,})\n")
        print(county_results)
        #Save the county results to the text file
        txt_file.write(county_results)
        
        #Determine the largest county turnout.
        if (votes_county > largest_county_count) and (vote_county_percentage > largest_coounty_percentage):
            # if true then set largest_county_count = votes_county and largest_coounty_percentage = vote_county_percentage
            largest_county_count = votes_county
            largest_coounty_percentage = vote_county_percentage
            # And, set the largest_county_turnout = county_name
            largest_county_turnout = county_name
    #Print Largest County Turnout
    largest_county_results = (
        f"\n------------------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"------------------------------------\n")
    print(largest_county_results)

    #Save the largest county turnout to the text file
    txt_file.write(largest_county_results)

    # Determine the percentage of the votes for each candidate by looping through the counts
    # 1. Iterate throught the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
            #4. Print the candidate name and percentage of votes
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

        



    
