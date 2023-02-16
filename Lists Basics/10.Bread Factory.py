LIMIT_ENERGY = 100
energy = 100
coins = 100

working_day_events = input().split("|")
number_of_events = 0

for elements in working_day_events:
    event, number = elements.split("-")
    number = int(number)
    if event == "rest":
        number_of_events += 1
        if energy == LIMIT_ENERGY:
            print("You gained 0 energy.")
            print(f"Current energy: {energy}.")
        else:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= number:
            number_of_events += 1
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
            continue
    else:
        if coins >= number:
            number_of_events += 1
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            break


if number_of_events == len(working_day_events):
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
