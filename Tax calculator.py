# The first value is the bracket in dollars, the second value is the rate at which money in that bracket is taxed at
taxBrackets = [(10000, 0), (30000, 0.1), (100000, 0.25), (99999999999, 0.4)]

print("Enter your income: ")
theInput = input()
income = int(theInput)

taxOwed = 0.00

for currentDollarBeingCounted in range(income+1):
    for bracket in taxBrackets:
        if currentDollarBeingCounted <= bracket[0]:
            taxOwed += bracket[1]
            taxOwed = round(taxOwed, 2)
            break


overAllTaxRate = round((taxOwed/income*100), 2)

print("You owe $" + str(taxOwed) + " in taxes. \n")
print("Your overall tax rate for your income of $" + str(income) + " is: " + str(overAllTaxRate) + "%.\n")


