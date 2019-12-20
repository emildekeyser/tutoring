def cashier(amount, coins):
    if amount <= 0 or len(coins) == 0:
        return 0
    coin = coins[0]
    if amount == coin:
        return cashier(amount, coins[1:]) + 1
    else:
        return cashier(amount - coin, coins) + cashier(amount, coins[1:])

def main():
    amount = int(input("Please give an amount: "))
    coins = [1,2,5]
    print(cashier(amount, coins))

main()
