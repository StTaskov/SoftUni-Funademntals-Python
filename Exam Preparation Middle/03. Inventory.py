def item_exist(it, inventory_list):
    if it in inventory_list:
        return True
    return False


items = input().split(", ")

command = input()

while not command == "Craft!":
    command, item = command.split(" - ")
    if command == "Collect":
        if item_exist(item, items):
            command = input()
            continue
        else:
            items.append(item)
    elif command == "Drop":
        if item_exist(item, items):
            items.remove(item)
        else:
            command = input()
            continue
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if item_exist(old_item, items):
            old_index = items.index(old_item)
            items.insert(old_index+1, new_item)
        else:
            command = input()
            continue
    elif command == "Renew":
        if item_exist(item, items):
            items.remove(item)
            items.append(item)
    command = input()

print(", ".join(items))
