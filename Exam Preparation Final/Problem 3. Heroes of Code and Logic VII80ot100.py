number_of_heroes = int(input())

hero_dict = {}

for _ in range(number_of_heroes):
    hero, hp, mana = input().split()
    if int(hp) < 0 or int(mana) < 0:
        continue
    else:
        hero_dict[hero] = {"HP": int(hp), "MP": int(mana)}

command = input()

while not command == "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        hero_name = command[1]
        mana_needed = int(command[2])
        spell_name = command[3]
        if hero_dict[hero_name]["MP"] < mana_needed:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            diff = hero_dict[hero_name]["MP"] - mana_needed
            hero_dict[hero_name]["MP"] -= mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {diff} MP!")
    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        hero_dict[hero_name]["HP"] = hero_dict[hero_name]["HP"] - damage
        if hero_dict[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_dict[hero_name]['HP']} HP left!")
        else:
            hero_dict.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif command[0] == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        diff = 200 - hero_dict[hero_name]["MP"]
        hero_dict[hero_name]["MP"] += amount
        if hero_dict[hero_name]["MP"] > 200:
            hero_dict[hero_name]["MP"] = 200
            print(f"{hero_name} recharged for {diff} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")
    elif command[0] == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        diff = 100 - hero_dict[hero_name]["HP"]
        hero_dict[hero_name]["HP"] += amount
        if hero_dict[hero_name]["HP"] > 100:
            hero_dict[hero_name]["HP"] = 100
            print(f"{hero_name} healed for {diff} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")
    command = input()

dict_for_print =sorted(hero_dict.items(), key=lambda tkvp: (tkvp[1]["HP"], tkvp[0]), reverse=True)
for index in range(len(dict_for_print)):
    print(dict_for_print[index][0])
    print(f"  HP: {dict_for_print[index][1]['HP']}")
    print(f"  MP: {dict_for_print[index][1]['MP']}")


