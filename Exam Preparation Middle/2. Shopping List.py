def it_exist(it, list):
    if it in list:
        return True
    return False


shopping_list = input().split("!")


command_data = input()
while not command_data == "Go Shopping!":
    command_data = command_data.split()

    if command_data[0] == "Urgent":
        if not it_exist(command_data[1], shopping_list):
            shopping_list.insert(0, command_data[1])
        else:
            command_data = input()
            continue
    elif command_data[0] == "Unnecessary":
        if it_exist(command_data[1], shopping_list):
            shopping_list.remove(command_data[1])
        else:
            command_data = input()
            continue
    elif command_data[0] == "Correct":
        old_name = command_data[1]
        new_item = command_data[2]
        if it_exist(old_name, shopping_list):
            old_index = shopping_list.index(old_name)
            shopping_list.remove(old_name)
            shopping_list.insert(old_index, new_item)
        else:
            command_data = input()
            continue
    elif command_data[0] == "Rearrange":
        if it_exist(command_data[1], shopping_list):
            shopping_list.remove(command_data[1])
            shopping_list.append(command_data[1])
    command_data = input()

print(", ".join(shopping_list))
