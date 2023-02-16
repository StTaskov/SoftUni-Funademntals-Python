number_of_commands = int(input())

user_dict = {}

for _ in range(number_of_commands):
    commands = input().split()
    if commands[0] == "register":
        if commands[1] in user_dict:
            print(f"ERROR: already registered with plate number {commands[2]}")
        else:
            user_dict[commands[1]] = commands[2]
            print(f"{commands[1]} registered {commands[2]} successfully")

    elif commands[0] == "unregister":
        if commands[1] not in user_dict:
            print(f"ERROR: user {commands[1]} not found")
        else:
            print(f"{commands[1]} unregistered successfully")
            user_dict.pop(commands[1])

for key, value in user_dict.items():
    print(f"{key} => {value}")

