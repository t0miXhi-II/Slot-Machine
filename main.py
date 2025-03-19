import random 

# Constant Variables (Written in all-caps)
MAX_LINE = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

machineSymbols = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def getValue(amount):
    while True:
        amount = input("Enter value: ")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a vlue greater than 0")
        else:
            print("Please enter a valid amoumt to proceed. ")

    return amount


def getBetAmount():
    while True:
        betAmount = input("Enter Bet amount for each line: AU$ ")

        if betAmount.isdigit():
            betAmount = int(betAmount)
            if MIN_BET <= betAmount <= MAX_BET:
                break
            else:
                print("Bet amount needs to be greater than 0")
        else:
            print("Please enter a valid amount")

    return betAmount


def getLineAmount():
    while True:
        lineAmount = input("Enter the amount of Lines you want to bet on: ")

        if lineAmount.isdigit():
            lineAmount = int(lineAmount)
            if 1 <= lineAmount <= MAX_LINE:
                break
            else:
                print("The Line value has to be greater than 0")
        else:
            print("Please enter a number")

    return lineAmount


def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: AU$ ")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit amount has to be greater than AU$0")
        else:
            print("Please enter a valid amoumt to proceed. ")

    return amount


def getSlotMachine(rows, cols, symbols):
    allSymbols = []

    for key, value in symbols.items():
        for _ in range(value):
            allSymbols.append(key)
    
    selectedColumns = []
    for _ in range(COLS):
        column = []
        symbolPool = allSymbols[:]

        for _ in range(ROWS):
            choice = random.choice(symbolPool)
            column.append(choice)
            symbolPool.remove(choice)

        selectedColumns.append(column)

    return selectedColumns


def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i < (len(columns) - 1):
                print(column[row], "|", end="")
            else:
                print(column[row], end="")
        print()


def checkWinings(columns, lines, bet, values):
    winings = 0
    wining_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolBeingChecked = column[line]
            if symbol != symbolBeingChecked:
                # print(f"No winings on Line {line + 1}.")
                break
        else:
            winings += values[symbol] * bet
            wining_lines.append(line + 1)

    return winings, wining_lines


def spin(balance):
    lineAmount = getLineAmount()

    while True:
        betAmount = getBetAmount()
        totalBetAmount = lineAmount * betAmount

        if totalBetAmount <= balance:
            break
        else:
            print(f"Insufficient Funds. Balance is AU${balance}.")

    print(f"Success! You have just placed a total bet of AU$ {totalBetAmount}")
    print(f"Bet is for AU${betAmount} on {lineAmount} lines")
    print()
    print("Loading Slot Machine....")
    print()

    slotSpin = getSlotMachine(ROWS, COLS, machineSymbols)
    printSlotMachine(slotSpin)
    winings, winingLines = checkWinings(slotSpin, lineAmount, betAmount, values)

    print(f"You have won AU$ {winings}.")
    print(f"Wining Line(s):", *winingLines)

    return winings - totalBetAmount


def main():
    balance = deposit()

    while True:
        startQuestion = input("press Enter to play or 'q' to quit: ")
        if startQuestion == 'q':
            break
        else:
            netBalance = spin(balance)
        
        balance += netBalance
        print(f"Current Balance: {balance}")

    
    


if __name__ == "__main__":
    main()



    # TEST CODE
    """ testMatrix = [["A", "B", "D", "D"], ["D", "C", "D", "A"], ["B", "B", "D", "C"]]

    for row in range(len(testMatrix)):
        for cols in testMatrix[row]:
            print(cols, "", end="")
        print()

    #for row in range(len(testMatrix[0])):
     #   for column in testMatrix:
      #      print(column[row])

    print()

    for row in range(len(testMatrix[0])):
        for column in testMatrix:
            print(column[row], "", end="")
        print() """

