products = input().split()
dictionary_products = {}

for index in range(0, len(products), 2):
    food = products[index]
    value = products[index+1]
    dictionary_products[food] = int(value)

print(dictionary_products)
