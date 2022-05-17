#add dependencies
#importing csv module so that we can use a csv file, importing os in case filepath is not known
import csv
import os

#assign variable to load file to path
file_to_load =os.path.join("Resources", "election_results.csv")
#assign variable to save file to path
file_to_save =os.path.join("Analysis", "election_analysis.txt")

#initialize total votes variable, candidate options list, and candidate votes dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}

#winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open elections file and read the file. Use with() instead of open() so that you don't have to close at end. file_to_load variable is referenced as file object throughout the code
with open(file_to_load) as election_data:
    print(election_data)
    #Do analysis here
    #read file object with reader function
    file_reader = csv.reader(election_data)
    headers = next(file_reader) #skipping headers. Do print(headers) to see them after this line
    
    #for row in filereader:
       # print(row[0])

##LIST OF DATA WE NEED TO GET
#Total number of votes cast
    for row in file_reader:
        total_votes = total_votes + 1
#A complete list of candidates who received votes
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
#Total number of votes each candidate received
            candidate_votes[candidate_name]= 0
        candidate_votes[candidate_name] =  candidate_votes[candidate_name] + 1
#Percentage of votes each candidate won
    #Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate  
        votes = candidate_votes[candidate_name] 
        # calculate percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
        # Print the candidate name and percentage of votes  
        ######print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")
#The winner of the election based on popular vote
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
#print out each candidates name, their vote count, and their percentage of votes
        print(f"{candidate_name}: {votes:,}, {vote_percentage:.1f}%\n")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)  

    #print(f"Number of total votes: {total_votes}")
    #print(f"These are the candidate options: {candidate_options}")
    #print(candidate_votes)
#outputing file to write analysis. Use with so that you don't have to have a closing statement. "W" is so you're writing in it
with open(file_to_save, "w") as txt_file:

    #write three countries to new file
    txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver")
    txt_file.write("\nJefferson")