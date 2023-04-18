# Import Dependencies
import os
import csv

# File Path
budget_csv = os.path.join('PyBank','Resources','budget_data.csv')

# Create empty lists for looping
total_months = []
total_profit = []
monthly_profit_change = []
 
# Open csv as read
with open(budget_csv, 'r') as csv_file:

     #Create csv reader
    csvreader = csv.reader(csv_file,delimiter=",") 

    # Skip the header labels 
    header = next(csvreader)  

    for row in csvreader:

        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for x in range(len(total_profit)-1):

        monthly_profit_change.append(total_profit[x+1]-total_profit[x])

    # max and min of profit change per month 
    max_increase = max(monthly_profit_change)
    min_increase = min(monthly_profit_change)

    month_max_increase = monthly_profit_change.index(max(monthly_profit_change))+1 # +1 adding one to index to give actual number of month
    month_min_increase = monthly_profit_change.index(min(monthly_profit_change))+1 # +1 adding one to index to give actual number of month

    #Printing Analysis 

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months {len(total_months)}")
    print(f"Total: {sum(total_profit)}")
    print(f"Average Change: ${round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}") #round lets you round to how many decimal places you want (2)
    print(f"Greatest Increase in Profits: {total_months[month_max_increase]} $({str(max_increase)})")
    print(f"Greatest Decrease in Profits: {total_months[month_min_increase]} $({str(min_increase)})")




financial_output = os.path.join('PyBank','Analysis','Financial_Analysis_Sum.txt')

with open(financial_output,"w") as file:
    
    # Write methods to print to Financial_Analysis_Summary 
    # ("\n") lets you skip to the next line 
    file.write("Financial Analysis")
    file.write('\n')
    file.write("----------------------------")
    file.write('\n')
    file.write(f"Total Months: {len(total_months)}")
    file.write('\n')
    file.write(f"Total: ${sum(total_profit)}")
    file.write('\n')
    file.write(f"Average Change: {round(sum(monthly_profit_change) / len(monthly_profit_change),2)}")
    file.write('\n')
    file.write(f"Greatest Increase in Profits: {total_months[month_max_increase]} (${(str(max_increase))})")
    file.write('\n')
    file.write(f"Greatest Decrease in Profits: {total_months[month_min_increase]} (${(str(min_increase))})")


