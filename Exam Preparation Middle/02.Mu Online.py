INITIAL_HEALTH = 100
health = 100
bitcoins = 0
count_of_rooms = 0

dungeon_rooms = input().split("|")

complete = True
for every_room in dungeon_rooms:
    count_of_rooms +=1
    command, number = every_room.split(" ")
    number = int(number)
    if command == "potion":
        if health < 100:
            health += number
            if health > INITIAL_HEALTH:
                print(f"You healed for {abs(number-(health - INITIAL_HEALTH))} hp.")
                health = 100
                print(f"Current health: {health} hp.")
            else:
                print(f"You healed for {number} hp.")
                print(f"Current health: {health} hp.")
        else:
            continue
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if not health <= 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {count_of_rooms}")
            complete = False
            break

if complete:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")