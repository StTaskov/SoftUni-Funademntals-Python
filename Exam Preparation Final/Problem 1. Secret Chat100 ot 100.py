message = input()
data = input()
mess = ""

while not data == "Reveal":
    data = data.split(":|:")
    if data[0] == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        for letter in message:
            if letter == substring:
                message = message.replace(substring, replacement)
                print(message)
                break
    elif data[0] == "Reverse":
        substring = data[1]
        if substring in message:
            message = message.replace(substring, "")
            substring = list(substring)
            message = list(message)
            substring = substring[::-1]
            message.extend(substring)
            message = "".join(message)
            print(message)
        else:
            print("error")
    elif data[0] == "InsertSpace":
        index = int(data[1])
        message_1 = message[:index]
        message_2 = message[index:]
        mess = message_1 + " " + message_2
        print(mess)
    data = input()
print(f"You have a new text message: {mess}")
