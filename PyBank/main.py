#print title
print('Financial Analysis')
print('-------------------------')

#READ CSV File
#import necessary modules
import os
import csv

#Variables
months = 0
net_amount = 0

#create path to csv
csvpybank = os.path.join("Resources", "budget_data.csv")

#open the csv
with open(csvpybank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #After the header, read each row    
    for row in csvreader:

        #Total number of months        
        months = months + 1

        #Net Amount of Profits/Losses
        net_amount = net_amount + int(row[1])


#Print your Data
print(f"Total Months: {months}")
print(f"Net Amount: {net_amount}")
