#Import OS and CSV Modules
import os
import csv
import numpy as np

#List Variables
voter_id = []
county = []
candidate = []
unique_candidate = []

#Create a filepath, open the file, read the file
csv_path = os.path.join('./', 'Resources', 'election_data.csv')
with open(csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
    #Skip the header row
    headerrow = next(csvreader)
    #convert the csvreader file to a list
    #csv_list = list(csvreader)
    
    #Loop through csvreader and append columns to separate lists
    for row in csvreader:
        voter_id.append(row[0])
        votes = len(voter_id)  #Answer: # of Total Votes
        county.append(row[1])
        candidate.append(row[2])

#Find unique candidates in candidate list using numpy, and append candidate names to unique candidate list
x = np.array(candidate)
unique_candidate.append(np.unique(x)) #This stores the unique candidates in the unique_candidate list

#Find the number of votes each candidate won
correy_votes = candidate.count("Correy") #Answer to total number of votes each candidate won
khan_votes = candidate.count("Khan") #Answer to total number of votes each candidate won
li_votes = candidate.count("Li") #Answer to total number of votes each candidate won
otooley_votes = candidate.count("O'Tooley") #Answer to total number of votes each candidate won

#Find the percentage-number of the total vote each candidate won
correy_per_num = correy_votes / votes
khan_per_num = khan_votes / votes
li_per_num = li_votes / votes
otooley_per_num = otooley_votes / votes

#Convert the precentage number to an actual percentage to the 3rd decimal point
correy_per = "{:.3%}".format(correy_per_num) #Answers to Percentage of Votes each candidate won
khan_per = "{:.3%}".format(khan_per_num) #Answers to Percentage of Votes each candidate won
li_per = "{:.3%}".format(li_per_num) #Answers to Percentage of Votes each candidate won
otooley_per = "{:.3%}".format(otooley_per_num) #Answers to Percentage of Votes each candidate won

#Create a total vote count list
vote_count = [correy_votes, khan_votes, li_votes, otooley_votes]

#Create a Dictionary of unique candidates and their total votes
vote_dict = {
    "Correy": correy_votes,
    "Khan": khan_votes,
    "Li": li_votes,
    "O'Tooley": otooley_votes
}

#Define a function that will return a key of a dictionary with the max value - Used Google-Fu
def keywithmaxval(d): 
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

#Assign result to the keywithmaxval function run on the vote dictionary
result = keywithmaxval(vote_dict) #Answers who won the election

#Print your analysis to the terminal
print("Election Results")
print("---------------------")
print(f"Total Votes: {votes}")
print("---------------------")
print(f"Khan: {khan_per} ({khan_votes})")
print(f"Correy: {correy_per} ({correy_votes})")
print(f"Li: {li_per} ({li_votes})")
print(f"O'Tooley: {otooley_per} ({otooley_votes})")
print("---------------------")
print(f"Winner: {result}")
print("---------------------")

#Create a filepath to export a text file
export_path = os.path.join('./', 'Analysis', 'analysis2.txt')

#Export filepath
with open(export_path, 'w') as analysis:
    analysis.write("Election Results\n")
    analysis.write("-------------------\n")
    analysis.write(f"Total Votes: {votes}\n")
    analysis.write("-------------------\n")
    analysis.write(f"Khan: {khan_per} ({khan_votes})\n")
    analysis.write(f"Correy: {correy_per} ({correy_votes})\n")
    analysis.write(f"Li: {li_per} ({li_votes})\n")
    analysis.write(f"O'Tooley: {otooley_per} ({otooley_votes})\n")
    analysis.write("-------------------\n")
    analysis.write(f"Winner: {result}\n")
    analysis.write("-------------------\n")


