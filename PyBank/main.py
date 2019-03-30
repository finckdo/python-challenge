import os
import csv

# use csv file from the Resources directory
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')  # read csv from Resources directory


# Open csv file from
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    csv_header = next(csvreader)  # skip header row from csv file

    #  Declare 2 new lists that are empty
    months = []
    profitloss = []

    # for each row in the csv file, append values from the first index to the new months list and the second index to the new profitloss index
    for row in csvreader:
        monthvalue=row[0]
        profitlossvalue=row[1]

        months.append(monthvalue)
        profitloss.append(int(profitlossvalue))  #  enforce data type for the new profit loss values is an integer


recordcount = len(profitloss)  # count length of the list created from the original csv file
TotalProfitLoss = (sum(profitloss))  # calculate total profit/loss
AverageProfitLoss = format((sum(profitloss)/ (len(profitloss))), '.2f')  # calculate average profit/loss and format to floating 2 decimal places


HighestProfitLoss = (max(profitloss))  # find max value from the profitloss list
HighestProfitDate = months[profitloss.index(HighestProfitLoss)]  #  use index from the max value from profitloss to find matching value in month list


LowestProfitLoss = (min(profitloss))  # find min value from the profitloss list
LowestProfitDate = months[profitloss.index(LowestProfitLoss)]  #  use index from the min value from profitloss to find matching value in month list

# Print output based on format from Readme file
print('')
print('Financial Analysis')
print('----------------------------')
print(f"Total Months: {recordcount}")
print(f"Total: ${TotalProfitLoss}")
print(f"Average: ${AverageProfitLoss}")
print(f"Greatest Increase in Profits: {HighestProfitDate} (${HighestProfitLoss})")
print(f"Greatest Decrease in Profits: {LowestProfitDate} (${LowestProfitLoss})")

#  Initialize output file
output_file = os.path.join("PyBank_output.txt")


with open(output_file, "w", encoding='utf-8') as datafile:
    writer = csv.writer(datafile, delimiter=' ')
    # writer = csv.writer(datafile)
    
    writer.writerow(['Financial Analysis'])
    writer.writerow(['-------------------------'])
    writer.writerow([f'Total Months: {recordcount}'])
    writer.writerow([f'Total: ${TotalProfitLoss}'])
    writer.writerow([f'Average: ${AverageProfitLoss}'])
    writer.writerow([f'Greatest Increase in Profits: {HighestProfitDate} (${HighestProfitLoss})'])
    writer.writerow([f'Greatest Decrease in Profits: {LowestProfitDate} (${LowestProfitLoss})'])
    


