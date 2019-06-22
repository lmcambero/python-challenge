import os
import csv

# Path to collect data from the source folder
financial_csv = os.path.join('PyBank_Resources_budget_data.csv')

# Read in the CSV file
with open(financial_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    months = []
    dinero = []
    money = []
    money_change = []

    for row in csvreader:
        months.append(row[0])
        dinero=float(row[1])
        money.append(dinero)
        for i in range(1,len(money)):
            money_change.append(money[i] - money[i-1])
            avg_change = sum(money_change)/len(money_change)
            max_change = max(money_change)
            min_change =min(money_change)

print("Financial Analysis\n----------------------------")

def contarmeses(list):
    return(len(months))

def total(list):
    return(round(sum(money)))

def promedio(list):
    return(round(avg_change))

def maximo(list):
    return(round(max_change))

def minimo(list):
    return(round(min_change))

print(f"Total Months: {contarmeses(list)}")
print(f"Total: ${total(list)}")
print(f"Average  Change: {promedio(list)}")
print(f"Greatest Increase in Profits: {maximo(list)}")
print(f"Greatest Decrease in Profits: {minimo(list)}")


file = open("main.txt","w+")

file.write("Financial Analysis\n----------------------------\n")
file.write(f"Total Months: {contarmeses(list)}\n")
file.write(f"Total: ${total(list)}\n")
file.write(f"Average  Change: {promedio(list)}\n")
file.write(f"Greatest Decrease in Profits: {minimo(list)}\n")

file.close()
