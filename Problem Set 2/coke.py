price = 50
coin_list = [5, 10, 25]
total_coin = 0


while price > total_coin:
    print(f"Amount Due: {price - total_coin}")

    coin = int(input("Insert coin: "))

    if coin in coin_list:
        total_coin += coin
    else:
        total_coin += 0

    while price <= total_coin:
        print(f"Change Owed: {total_coin - price}")
        break