product = input()
product_dictionary = {}

while not product == "statistics":
    food, value = product.split(": ")
    value = int(value)
    if food in product_dictionary:
        product_dictionary[food] += value
    else:
        product_dictionary[food] = value
    product = input()

print("Products in stock:")
for every_product in product_dictionary:
    print(f"- {every_product}: {product_dictionary[every_product]}")
print(f"Total Products: {len(product_dictionary)}")
print(f"Total Quantity: {sum(product_dictionary.values())}")
