import os
import csv

# Defineing the path to the CSV file in the Resources folder
script_dir = os.path.dirname(os.path.realpath(__file__))

csv_path = os.path.join(script_dir, "Resources", "budget_data.csv")

# Initializing variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []

# Readimg the CSV file
with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skiping the header row
    header = next(csv_reader)
    
    # Looping through the rows in the CSV file
    for row in csv_reader:
        # Extracting date and profit/loss from the row
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculating total months and net total
        total_months += 1
        net_total += profit_loss
        
        # Calculating the change in profit/loss and store it in the list
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
        
        # Updating previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculating the average change
average_change = sum(changes) / len(changes)

# Finding the greatest increase and decrease
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Printing the analysis results in terminal
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Exporting the analysis results to a text file
output_file_path = os.path.join(script_dir, "financial_analysis.txt")
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print(f"Results have been saved to {output_file_path}")

