import pandas as pd 
import numpy as np

election_df = pd.read_csv("C:\\Users\\Setup\\Desktop\\Simon-Rice\\Homework\\python-challenge\\PyPoll\\Analysis\\election_data.csv")
#print(election_df)

#Print Total # of Votes
print(len(election_df))

#Candidates who recieved votes
candidate_list = election_df.Candidate.unique()
print(candidate_list)

#Candidate Vote Count
candidate_votes = election_df['Candidate'].value_counts()
print(candidate_votes)

khan_percent = candidate_votes['Khan'] / len(election_df)
print(khan_percent)

