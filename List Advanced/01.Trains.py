waggons = int(input())
train = [0] * waggons

command = input()

while not command == "End":
    command = command.split()
    if command[0] == "add":
        train[-1] += int(command[1])
    elif command[0] == "insert":
        train[int(command[1])] += int(command[-1])
    elif command[0] == "leave":
        train[int(command[1])] -= int(command[-1])
    command = input()

print(train)