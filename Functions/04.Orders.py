def total_price_for_products(pro, q):
    total_price = 0
    if pro == "coffee":
        total_price = 1.50 * q
    elif pro == "coke":
        total_price = 1.40 * q
    elif pro == "water":
        total_price = 1 * q
    elif pro == "snacks":
        total_price = 2.00 * q
    return f"{total_price:.2f}"


product = input()
quantity = int(input())

print(total_price_for_products(product, quantity))
