#add dependencies
#importing csv module so that we can use a csv file, importing os in case filepath is not known
import csv
import os

#assign variable to load file to path
file_to_load =os.path.join("Resources", "election_results.csv")
#assign variable to save file to path
file_to_save =os.path.join("Analysis", "election_analysis.txt")

#open elections file and read the file. Use with() instead of open() so that you don't have to close at end. file_to_load variable is referenced as file object throughout the code
with open(file_to_load) as election_data:
    print(election_data)
    #Do analysis here
    #read file object with reader function
    file_reader = csv.reader(election_data)
    headers = next(file_reader) #skipping headers. Do print(headers) to see them after this line
    
    #for row in filereader:
       # print(row[0])

##LIST OF DATS WE NEED TO GET
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

#outputing file to write analysis. Use with so that you don't have to have a closing statement. "W" is so you're writing in it
with open(file_to_save, "w") as txt_file:

    #write three countries to new file
    txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver")
    txt_file.write("\nJefferson")