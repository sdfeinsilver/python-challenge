#print title
print('Financial Analysis')
print('-------------------------')

#READ CSV File
#import necessary modules
import os
import csv

#Variables
months = 0




#create path to csv
csvpybank = os.path.join("Resources", "budget_data.csv")

#open the csv
with open(csvpybank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        months = months + 1
print(f"Total Months: {months}")