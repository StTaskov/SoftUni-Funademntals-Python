command_data = input()
shop_dict = {}
total_price_dict = {}

while not command_data == "buy":
    name, price, quantity = command_data.split()
    price = float(price)
    quantity = int(quantity)
    if name not in shop_dict:
        shop_dict[name] = {"price": price, "quantity": quantity}
    else:
        shop_dict[name]["price"] = price
        shop_dict[name]["quantity"] += quantity
    command_data = input()

for keys in shop_dict:
    total_price = shop_dict[keys]["price"] * shop_dict[keys]["quantity"]
    total_price_dict[keys] = total_price

for key, value in total_price_dict.items():
    print(f"{key} -> {value:.2f}")
