message = input()
data = input()

while not data == "Decode":
    data = data.split('|')
    if data[0] == "Move":
        number_of_letters = int(data[1])
        thing_for_append = message[:number_of_letters]
        message = message.replace(thing_for_append, "")
        message = message + thing_for_append
    elif data[0] == "Insert":
        index = int(data[1])
        value = data[2]
        message_list = []
        for char in message:
            message_list.append(char)
        message_list.insert(index, value)
        message = "".join(message_list)
    elif data[0] == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)
    data = input()

print(f"The decrypted message is: {message}")