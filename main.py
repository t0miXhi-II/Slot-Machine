import random 

# Constant Variables (Written in all-caps)
MAX_LINE = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbols = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
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

        selectedColumns.apppend(column)

    return selectedColumns


def main():
    balance = deposit()
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
    


if __name__ == "__main__":
    main()

# main()
