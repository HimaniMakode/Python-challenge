import os
import csv

print("Financial Analysis")
print("-----------------------------------------")

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # to skip header
    csv_reader = next(csvreader)

    totalProfitLoss = 0
    CountMonth = 0
    DateList = list()
    ProfitLossList = list()

    for row in csvreader:
        # counting number of months
        CountMonth = CountMonth + 1

        # calculating total profit/losses
        ProfitLoss = row[1]
        value = int(ProfitLoss)
        totalProfitLoss = totalProfitLoss + value

        ProfitLossList.append(int(row[1]))
        DateList.append(row[0])

    # find average change
    change_profitLoss = []

    for x in range(1, len(ProfitLossList)):
        change_profitLoss.append((int(ProfitLossList[x]) - int(ProfitLossList[x - 1])))

    # calculate average of the changes in "Profit/Losses"
    average_change = sum(change_profitLoss) / len(change_profitLoss)

    # Calculating greatest increase & decrease in "Profit/Losses"
    greatest_increase = max(change_profitLoss)
    greatest_decrease = min(change_profitLoss)

    print("Total Months: " + str(CountMonth))
    print("Total Profit/Loss: " + "$" + str(totalProfitLoss))
    print("Average change: " + "$" + str(average_change))
    print("Greatest Increase in Profits: " + str(DateList[change_profitLoss.index(max(change_profitLoss)) + 1]) + " " + "(" + "$" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(DateList[change_profitLoss.index(min(change_profitLoss)) + 1]) + " " + "(" + "$" + str(greatest_decrease) + ")")


# output to a text file

    file = open("output.txt", "w")
    file.write("Financial Analysis" + "\n")
    file.write("...................................................................................." + "\n")
    file.write("Total months: " + str(CountMonth) + "\n")
    file.write("Total Profit/Loss: " + "$" + str(totalProfitLoss) + "\n")
    file.write("Average change: " + "$" + str(average_change) + "\n")
    file.write("Greatest Increase in Profits: " + str(DateList[change_profitLoss.index(max(change_profitLoss)) + 1]) + " " + "(" + "$" + str(greatest_increase) + ")" + "\n")
    file.write("Greatest Decrease in Profits: " + str(DateList[change_profitLoss.index(min(change_profitLoss)) + 1]) + " " + "(" + "$" + str(greatest_decrease) + ")" + "\n")
    file.close()
