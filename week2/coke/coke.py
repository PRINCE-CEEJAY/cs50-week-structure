balance = 50

while balance > 0:
    print(f"Amount Due: {balance}")
    coin_request = int(input("input a coin ").strip())

    if coin_request in [25, 10, 5]:
        balance -= coin_request

print(f"Change Owed: {abs(balance)}")



