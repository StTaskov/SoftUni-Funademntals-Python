def is_index_valid(index, string):
    if 0 <= index < len(string):
        return True
    return False


text = input()

command = input()
while not command == "Finish":
    command = command.split()
    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        text = text.replace(current_char, new_char)
        print(text)
    elif command[0] == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        if not is_index_valid(start_index, text) or not is_index_valid(end_index, text):
            print("Invalid indices!")
        else:
            substring = text[start_index:end_index+1]
            text = text.replace(substring, "")
            print(text)
    elif command[0] == "Make":
        if command[1] == "Upper":
            text = text.upper()
            print(text)
        else:
            text = text.lower()
            print(text)
    elif command[0] == "Check":
        string = command[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif command[0] == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        if not is_index_valid(start_index, text) or not is_index_valid(end_index, text):
            print("Invalid indices!")
        else:
            substring = text[start_index:end_index+1]
            sum_of_letters = [ord(char) for char in substring]
            print(sum(sum_of_letters))
    command = input()