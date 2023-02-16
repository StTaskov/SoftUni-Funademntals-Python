password = input()
command = input()

while not command == "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        password = [password[index] for index in range(1, len(password), 2)]
        password = "".join(password)
        print(password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        substring = password[index:index+length]
        password = password.replace(substring, "", 1)
        print(password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {password}")
