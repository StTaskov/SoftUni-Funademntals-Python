activation_key = input()

command = input()
while not command == "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == "Upper":
            substring = activation_key[start_index:end_index]
            for_replace = substring.upper()
            activation_key = activation_key.replace(substring, for_replace)
        else:
            substring = activation_key[start_index:end_index]
            for_replace = substring.lower()
            activation_key = activation_key.replace(substring, for_replace)
        print(activation_key)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        first_part = activation_key[:start_index]
        second_part = activation_key[end_index:]
        activation_key = first_part + second_part
        print(activation_key)
    command = input()

print(f"Your activation key is: {activation_key}")
