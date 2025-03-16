# Constant Variables (Written in all-caps)
MAX_LINE = 3
MIN_BET = 1
MAX_BET = 100


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




def main():
    balance = deposit()
    betAmount = getBetAmount()
    lineAmount = getLineAmount()
    totalBetAmount = lineAmount * getBetAmount

    
    pass


#if __name__ == "__main__":
#    main()

main()
