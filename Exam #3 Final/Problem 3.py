peter_dict = {}

command = input()
while not command == "Log out":
    if command.startswith("New follower"):
        command = command.split(":")
        username = command[1]
        if username not in peter_dict:
            peter_dict[username] = 0
        else:
            command = input()
            continue
    elif command.startswith("Like:"):
        command = command.split(":")
        username = command[1]
        count = int(command[2])
        if username not in peter_dict:
            peter_dict[username] = 0
            peter_dict[username] += count
        else:
            peter_dict[username] += count
    elif command.startswith("Comment:"):
        command = command.split(":")
        username = command[1]
        if username not in peter_dict:
            peter_dict[username] = 0
            peter_dict[username] += 1
        else:
            peter_dict[username] += 1
    elif command.startswith("Blocked:"):
        command = command.split(":")
        username = command[1]
        if username in peter_dict:
            peter_dict.pop(username)
        else:
            print(f"{username} doesn't exist.")
    command = input()


peter_dict = sorted(peter_dict.items(), key=lambda tkvp: (-tkvp[1], tkvp[0]))
print(f"{len(peter_dict)} followers")
for k, v in peter_dict:
    print(f" {k}: {v}")
