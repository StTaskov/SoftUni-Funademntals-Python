budget = float(input())
flour_price = float(input())

colored_eggs_count = 0
current_count_of_cozunac = 0  # This is for print at the end.
count_of_cozunac = 0
losted_eggs = 0

egg_price = flour_price * 0.75
milk_price_l = flour_price + (flour_price * 0.25)
milk_price_4 = milk_price_l / 4
price_for_one_cozunac = flour_price + egg_price + milk_price_4

while price_for_one_cozunac <= budget:
    count_of_cozunac += 1
    current_count_of_cozunac += 1
    colored_eggs_count += 3
    budget -= price_for_one_cozunac

    if current_count_of_cozunac % 3 == 0:
        losted_eggs += count_of_cozunac - 2


money_left = budget
colored_eggs_count -= losted_eggs
print(f"You made {current_count_of_cozunac} cozonacs! Now you have {colored_eggs_count} eggs and {money_left:.2f}BGN left.")
