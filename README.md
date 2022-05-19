# Election_Analysis

## Description of project:
A colorado board of elections employee has given voting data and tasks to perform on it for a local election:

1. Calculate total votes in election
2. A complete list of candidates who received votes
3. Total number of votes each candidate recieved
4. Percentage of votes each candidate won
5. The winner of the election, based on popular vote
6. Number of votes and percentage of the total votes by county
7. County with the largest number of votes

## Resources used:
1. Python version 3.8.9, Visual Studio Code version 1.67.1
2. Data source: election_results.csv

## Results:
- Total votes = 369,711
- Candidate list = Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane
- Total number of votes and percentage of votes each candidate received:
  -  Charles Casper Stockham: 85,213, 23.0%
  -  Diana DeGette: 272,892, 73.8%
  -  Raymon Anthony Doane: 11,606, 3.1%
- Winner of the election: Diana DeGette, who received 272,892 votes and 73.8% of the vote
- Total number of votes and percentage of votes by county:
  - Jefferson: (38,855), 10.5%
  - Denver: (306,055), 82.8%
  - Arapahoe: (24,801), 6.7%
- County with largest number of votes: Denver

## Summary
This code could be reused (with some modifications) for any election. There are design patterns used in this code that could be universally applied:
  - finding the total votes by: setting a variable = 0, putting the variable through a for loop, and adding 1 each time it goes through an item in the list
  - getting a list of the candidates by: accessing one column in a data set (by using a for loop to go through a dictionary, and telling python to access one index in the list), starting a new candidate options variable outside of the loop, and adding to the list if a candidate is not in the candidate options list
  - determining a county with the largest number of votes (or just generally finding the largest number in a set of numbers) by: iterating through the candidate list, finding the number of votes per candidate, and writing an if statement that says if the votes of a candidate are greater than the winning number of votes (newly created variable), then that number of votes becomew the winning number of votes. 
Using these patterns, we could take other election data and perform the same tasks, after cleaning the data and putting it in a list of dictionaries format. 

