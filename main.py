
def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: AU$ ")

        if amount.isdigit():
            amount = int(amount)
        else:
            print("Please enter a valid amoumt to proceed. ")

        return amount

