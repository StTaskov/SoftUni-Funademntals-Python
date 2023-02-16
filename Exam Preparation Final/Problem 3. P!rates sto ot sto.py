def is_empty(dictionary):
    if dictionary:
        return True
    return False


town_data = input()

town_dict = {}

while not town_data == "Sail":
    town, population, gold = town_data.split("||")
    population = int(population)
    gold = int(gold)

    if town not in town_dict:
        town_dict[town] = {"population": population, "gold": gold}
    else:
        town_dict[town]["population"] += population
        town_dict[town]["gold"] += gold
    town_data = input()

command_data = input()

while not command_data == "End":
    command_data = command_data.split("=>")
    if command_data[0] == "Plunder":
        if command_data[1] in town_dict:
            town_dict[command_data[1]]["population"] -= int(command_data[2])
            town_dict[command_data[1]]["gold"] -= int(command_data[3])
            print(f"{command_data[1]} plundered! {command_data[3]} gold stolen, {command_data[2]} citizens killed.")
            if town_dict[command_data[1]]["population"] == 0 or town_dict[command_data[1]]["gold"] == 0:
                town_dict.pop(command_data[1])
                print(f"{command_data[1]} has been wiped off the map!")
    if command_data[0] == "Prosper":
        command_data[2] = int(command_data[2])
        if command_data[2] < 0:
            print("Gold added cannot be a negative number!")
            command_data = input()
            continue
        else:
            command_data[2] = int(command_data[2])
            town_dict[command_data[1]]["gold"] += command_data[2]
            print(f"{command_data[2]} gold added to the city treasury. {command_data[1]} now has {town_dict[command_data[1]]['gold']} gold.")
    command_data = input()


if is_empty(town_dict):
    print(f"Ahoy, Captain! There are {len(town_dict)} wealthy settlements to go to:")
    cities_dict = dict(sorted(town_dict.items(), key=lambda kvp: (- kvp[1]["gold"], kvp[0])))
    for target, value in cities_dict.items():
        print(f"{target} -> Population: {cities_dict[target]['population']} citizens, Gold: {cities_dict[target]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")