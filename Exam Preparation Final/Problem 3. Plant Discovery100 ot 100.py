number_of_plants = int(input())

plant_dict = {}

for _ in range(number_of_plants):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    if plant in plant_dict:
        plant_dict[plant]['rarity'] += int(rarity)
    else:
        plant_dict[plant] = {'rarity': rarity, 'avg_rating': []}

command = input()
while not command == "Exhibition":
    if command.startswith("Rate:"):
        command = command.split()
        rating = int(command[3])
        if command[1] in plant_dict:
            plant_dict[command[1]]['avg_rating'].append(rating)
        else:
            print("error")
    elif command.startswith("Update:"):
        command = command.split()
        new_rarity = int(command[3])
        if command[1] in plant_dict:
            plant_dict[command[1]]['rarity'] = new_rarity
        else:
            print('error')
    elif command.startswith("Reset:"):
        command = command.split()
        plant = command[1]
        if plant in plant_dict:
            plant_dict[plant]['avg_rating'].clear()
        else:
            print("error")
    else:
        print("error")
    command = input()

for value in plant_dict.values():
    if len(value["avg_rating"]) > 0:
       value['avg_rating'] = float(sum(value['avg_rating']) / len(value['avg_rating']))
    else:
        value['avg_rating'] = 0
for_print = sorted(plant_dict.items(), key=lambda tkvp: (tkvp[1]['rarity'], tkvp[1]['avg_rating']), reverse=True)
print("Plants for the exhibition:")
for el in for_print:
    print(f"- {el[0]}; Rarity: {el[1]['rarity']}; Rating: {el[1]['avg_rating']:.2f} ")
