def it_exist(it, lst):
    if it in lst:
        return True
    return False


painting_number = input().split()

command_data = input()
while not command_data == "END":
    command_data = command_data.split()
    if command_data[0] == "Change":
        if it_exist(command_data[1], painting_number):
            if it_exist(command_data[1], painting_number):
                paint_index = painting_number.index(command_data[1])
                painting_number.insert(paint_index, command_data[2])
                painting_number.remove(command_data[1])
    elif command_data[0] == "Hide":
        if it_exist(command_data[1], painting_number):
            painting_number.remove(command_data[1])
    elif command_data[0] == "Switch":
        if it_exist(command_data[1], painting_number) and it_exist(command_data[2], painting_number):
            first_number_index = painting_number.index(command_data[1])
            second_number_index = painting_number.index(command_data[2])
            painting_number.remove(command_data[1])
            painting_number.remove(command_data[2])
            painting_number.insert(first_number_index, command_data[2])
            painting_number.insert(second_number_index, command_data[1])
    elif command_data[0] == "Insert":
        place_index = int(command_data[1])
        if place_index < len(painting_number):
            painting_number.insert(place_index + 1, command_data[2])
    elif command_data[0] == "Reverse":
        painting_number.reverse()
    command_data = input()
print(" ".join(painting_number))
