number_of_cars = int(input())

cars_dict = {}

for _ in range(number_of_cars):
    car, millage, fuel = input().split("|")
    cars_dict[car] = {"millage": int(millage), "fuel": int(fuel)}

command = input()
while not command == "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        if cars_dict[command[1]]["fuel"] < int(command[3]):
            print("Not enough fuel to make that ride")
        else:
            cars_dict[command[1]]["millage"] += int(command[2])
            cars_dict[command[1]]["fuel"] -= int(command[3])
            print(f"{command[1]} driven for {command[2]} kilometers. {command[3]} liters of fuel consumed.")
        if cars_dict[command[1]]["millage"] >= 100000:
            cars_dict.pop(command[1])
            print(f"Time to sell the {command[1]}!")
    elif command[0] == "Refuel":
        current_car = command[1]
        fuel_to_add = int(command[2])
        max_capacity = 75
        if fuel_to_add > max_capacity - cars_dict[command[1]]["fuel"]:
            print(f"{current_car} refueled with {max_capacity - cars_dict[command[1]]['fuel']} liters")
            cars_dict[command[1]]["fuel"] += max_capacity - cars_dict[command[1]]["fuel"]

        else:
            cars_dict[command[1]]["fuel"] += fuel_to_add
            print(f"{current_car} refueled with {fuel_to_add} liters")

    elif command[0] == "Revert":
        current_car = command[1]
        millage_to_decrease = int(command[2])
        cars_dict[current_car]["millage"] -= millage_to_decrease
        if cars_dict[current_car]["millage"] <= 10000:
            cars_dict[current_car]["millage"] = 10000
        else:
            print(f"{current_car} mileage decreased by {millage_to_decrease} kilometers")
    command = input()

dict_for_print = sorted(cars_dict.items(), key=lambda tkvp: (-tkvp[1]['millage'], tkvp[0]))

for key, value in dict_for_print:
    print(f"{key} -> Mileage: {value['millage']} kms, Fuel in the tank: {value['fuel']} lt.")
