amount_due = 50

while amount_due > 0:
    coin = int(input("Insert coin: "))

    if coin in [25, 10, 5]:
        amount_due -= coin

        if amount_due > 0:
            print(f"Amount due: {amount_due}")
        elif amount_due == 0:
            print("Exact amount.")
        else:
            print(f"Change owed: {-amount_due}")
    