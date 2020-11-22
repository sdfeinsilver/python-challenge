#import modules
import os
import csv

#Variables
months = 0
net_amount = 0

#create path to csv
csvpybank = os.path.join("./", "Resources", "budget_data.csv")

#Read the CSV and skip the header row
with open(csvpybank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #Create List to add monthly changes
    change_list = []

    #Convert to list
    csvreader = list(csvreader)

    #Starting Your loop and analyzing

    for i in range(len(csvreader)):
        
        #Total number of months 
        months = months + 1 
        #Net Amount of Profits/Losses
        net_amount += int(csvreader[i][1])
        #Calculate monthly change
        if i > 0:
            monthly_change = int(csvreader[i][1]) - int(csvreader[i-1][1])
            change_list.append(monthly_change)
    calc_avg = sum(change_list) / (len(change_list))
    max_profit = max(change_list)
    max_index = change_list.index(max_profit)
    max_month = csvreader[max_index + 1][0]
    
    min_profit = min(change_list)
    min_index = change_list.index(min_profit)
    min_month = csvreader[min_index + 1][0]

#print title
print('Financial Analysis')
print('-------------------------')


#Print your Data
print(f"Total Months: {months}")
print(f"Net Amount: {net_amount}")
print(f"Average Change: {calc_avg}")
print(f"Greatest Increase in Profits: {max_month} " + f"({max_profit})")
print(f"Greatest Decrease in Profits: {min_month} " + f"({min_profit})")

#Print Results to text file
output_file = os.path.join('./', 'Analysis', 'analysis.txt')
with open(output_file, 'w', newline='') as text_file:
    text_file.write('Financial Analysis')
    text_file.write("\n")
    text_file.write('-------------------------')
    text_file.write("\n")
    text_file.write("\n")
    text_file.write(f"Total Months: {months}")
    text_file.write("\n")
    text_file.write(f"Net Amount: {net_amount}")
    text_file.write("\n")
    text_file.write(f"Average Change: {calc_avg}")
    text_file.write("\n")
    text_file.write(f"Greatest Increase in Profits: {max_month} " + f"({max_profit})")
    text_file.write("\n")
    text_file.write(f"Greatest Decrease in Profits: {min_month} " + f"({min_profit})")