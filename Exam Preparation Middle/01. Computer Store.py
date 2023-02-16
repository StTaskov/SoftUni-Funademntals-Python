price_for_part = input()

price_for_all_parts_without_tax = 0
final_price = 0
customer = ""


while not price_for_part == "special" and not price_for_part == "regular":
    price_for_part = float(price_for_part)
    if price_for_part >= 0:
        price_for_all_parts_without_tax += price_for_part
    else:
        print("Invalid price!")
        price_for_part = input()
        continue
    price_for_part = input()

if price_for_part == "special":
    customer = "special"
if price_for_part == "regular":
    customer = "regular"

if final_price >= 0:
    final_price = price_for_all_parts_without_tax + price_for_all_parts_without_tax * 0.2
else:
    print("Invalid order!")

if customer == "special":
    final_price -= final_price * 0.1

if final_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_for_all_parts_without_tax:.2f}$")
    print(f"Taxes: {(price_for_all_parts_without_tax * 0.2):.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")
