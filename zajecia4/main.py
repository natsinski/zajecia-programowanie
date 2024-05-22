prices_in_dollars = [2.40, 999, 34.21, 150, 1001]
def change_to_dollars(price):
    price = str(price)
    return "$" + price

result = list(map(change_to_dollars, prices_in_dollars))

print(result)