places = input()

command = input()
while not command == "Travel":
    if "Switch" in command:
        command = command.split(":")
    else:
        command = command.split()

    if command[0] == "Add":
        second_lst = command[1].split(":")
        index = int(second_lst[1])
        string = second_lst[2]
        index_list = [char for char in places]
        if 0 <= index > len(index_list):
            pass
        else:
            index_list.insert(index, string)
            places = "".join(index_list)
        print(places)
    elif command[0] == "Remove":
        second_lst = command[1].split(":")
        start_index = int(second_lst[1])
        end_index = int(second_lst[2])
        index_list = [char for char in places]
        if 0 <= start_index > len(index_list) and 0 <= end_index > len(index_list):
            pass
        else:
            places = "".join(index_list)
            part_for_remove = places[start_index:end_index+1]
            places = places.replace(part_for_remove, "")
        print(places)
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        while old_string in places:
            places = places.replace(old_string, new_string)
        print(places)
    command = input()

print(f"Ready for world tour! Planned stops: {places}")