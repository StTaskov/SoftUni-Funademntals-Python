numbers = [int(num) for num in input().split()]

command_data = input()

while not command_data == "end":
    command_data = command_data.split()
    if command_data[0] == "reverse":
        start_index = int(command_data[2])
        end_index = int(command_data[4])
        needed_numbers = numbers[start_index:end_index+2]
        del(numbers[start_index:end_index])
        numbers[start_index:len(needed_numbers)] = reversed(needed_numbers)
    elif command_data[0] == "sort":
        start_index = int(command_data[2])
        end_index = int(command_data[4])
        needed_numbers = numbers[start_index:end_index+2]
        del(numbers[start_index:end_index+1])
        numbers[start_index:len(needed_numbers)-1] = sorted(needed_numbers)
    elif command_data[0] == "remove":
        end_index = int(command_data[1])
        needed_numbers = numbers[0:end_index]
        del(numbers[0:end_index])
    command_data = input()

print(*numbers, sep=", ")
