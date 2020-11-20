#print title
print('Financial Analysis')
print('-------------------------')

#READ CSV File
#import necessary modules
import os
import csv

#Lists to store data
months = []




#create path to csv
csvpybank = os.path.join("Resources", "budget_data.csv")

#open the csv
with open(csvpybank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        print(row)
