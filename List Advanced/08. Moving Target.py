def it_target_is_valid(lst, ind):
    if len(lst) > ind >= 0:
        return True
    return False


target_sequence_with_value = [int(numbers) for numbers in input().split()]
command = input()

while not command == "End":
    command = command.split()
    command[1] = int(command[1])
    command[2] = int(command[2])
    if command[0] == "Shoot":
        if it_target_is_valid(target_sequence_with_value, command[1]):
            target_sequence_with_value[command[1]] -= command[2]
            if target_sequence_with_value[command[1]] <= 0:
                target_sequence_with_value.remove(target_sequence_with_value[command[1]])
    if command[0] == "Add":
        if it_target_is_valid(target_sequence_with_value, command[1]):
            target_sequence_with_value.insert(command[1], command[2])
        else:
            print("Invalid placement!")
    if command[0] == "Strike":
        if it_target_is_valid(target_sequence_with_value, command[1]):
            if (command[1] - command[2]) in range(0, len(target_sequence_with_value)) and (command[1] + command[2]) in range(0, len(target_sequence_with_value)):
                del target_sequence_with_value[(command[1] - command[2]): (command[1] + command[2]) + 1]
            else:
                print("Strike missed!")
        else:
            print("Strike missed!")
    command = input()

print(*target_sequence_with_value, sep="|")
