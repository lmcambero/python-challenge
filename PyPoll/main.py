import os
import csv

# Path to collect data from the source folder
elections_csv = os.path.join('election_data.csv')

# Read in the CSV file
with open(elections_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    votes = []
    candidates = []
#    money = []
#    money_change = []

    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
#        money.append(dinero)
        for i in range(1,(candidates)):

#            money_change.append(money[i] - money[i-1])
#            avg_change = sum(money_change)/len(money_change)
#            max_change = max(money_change)
#            min_change =min(money_change)

print("Election Results\n-------------------------")

def contarvotos(list):
    return(len(votes))

#def total(list):
#    return(round(sum(money)))

#def promedio(list):
#    return(round(avg_change))

#def maximo(list):
#    return(round(max_change))

#def minimo(list):
#    return(round(min_change))

print(f"Total Votes: {contarvotos(list)}")
#print(f"Total: ${total(list)}")
#print(f"Average  Change: {promedio(list)}")
#print(f"Greatest Increase in Profits: {maximo(list)}")
#print(f"Greatest Decrease in Profits: {minimo(list)}")


file = open("main.txt","w+")

file.write("Election Results\n-------------------------\n")
file.write(f"Total votes: {contarvotos(list)}\n")
#file.write(f"Total: ${total(list)}\n")
#file.write(f"Average  Change: {promedio(list)}\n")
#file.write(f"Greatest Decrease in Profits: {minimo(list)}\n")

file.close()
