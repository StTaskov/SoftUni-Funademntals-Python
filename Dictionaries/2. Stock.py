products = input().split()
products_dictionary = {}

for index in range(0, len(products), 2):
    product = products[index]
    value = products[index+1]
    products_dictionary[product] = int(value)

searched_products = input().split()

for every_product in searched_products:
    if every_product in products_dictionary:
        print(f"We have {products_dictionary[every_product]} of {every_product} left")
    else:
        print(f"Sorry, we don't have {every_product}")
