gifts = input().split(" ")

big_command = input()
while not big_command == "No Money":
    command, value = big_command.split()
    if command == "OutOfStock" and value in gifts:
        for elements in gifts:
            if value == elements:
                gifts.remove(elements)
                gift_index = gifts.index(elements)
                gifts.insert([gift_index], None)
    elif command

