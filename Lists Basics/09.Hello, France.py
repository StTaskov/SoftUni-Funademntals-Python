items = input().split("|")
budget = float(input())

list_with_the_new_prices = []
profit_like_all = 0

for elements in items:
    type, price = elements.split("->")
    price = float(price)

    if type == "Clothes" and price > 50.00:
        continue
    elif type == "Shoes" and price > 35.00:
        continue
    elif type == "Accessories" and price > 20.50:
        continue
    else:
        if budget >= price:
            budget -= price
            profit = price * 0.4
            profit_like_all += profit
            list_with_the_new_prices.append(price)
        else:
            continue

for el in list_with_the_new_prices:
    print(f"{el:.2f} ", end='')
print(f"Profit: {profit_like_all:.2f}")

budget += sum(list_with_the_new_prices)

if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
