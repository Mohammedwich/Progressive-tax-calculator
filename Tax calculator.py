# These are the tax brackets for $10k, $30k, $100k, and over $100k
taxBracket10k = 0
taxBracket30k = 0.1
taxBracket100k = 0.25
taxBracketOver100k = 0.4

print("Enter your income: ")
theInput = input()
income = int(theInput)

taxOwed = 0.00

for currentDollarBeingCounted in range(income+1):
    if currentDollarBeingCounted <= 10000:
        taxOwed += 0
    elif currentDollarBeingCounted <= 30000:
        taxOwed += 0.1
    elif currentDollarBeingCounted <= 100000:
        taxOwed += 0.25
    else:
        taxOwed += 0.40

    taxOwed = round(taxOwed, 2)

overAllTaxRate = round((taxOwed/income*100), 2)

print("You owe $" + str(taxOwed) + " in taxes. \n")
print("Your overall tax rate for your income of $" + str(income) + " is: " + str(overAllTaxRate) + "%.\n")


