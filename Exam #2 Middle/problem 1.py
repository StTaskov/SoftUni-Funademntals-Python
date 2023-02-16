count_of_orders = int(input())
total_price = 0

for each_order in range(1, count_of_orders+1):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())

    price_like_all = ((days * capsule_count) * price_per_capsule)
    total_price += price_like_all
    print(f"The price for the coffee is: ${price_like_all:.2f}")
print(f"Total: ${total_price:.2f}")
