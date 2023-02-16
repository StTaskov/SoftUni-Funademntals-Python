materials = input()

key_materials = {"shards": 0, "motes": 0, "fragments": 0}
junks = {}
key = False
legendary_item = ""

while not key:
    materials = materials.split()
    for index in range(0, len(materials), 2):
        if key:
            break

        material = materials[index+1].lower()
        quantity = int(materials[index])

        if material in key_materials:
            key_materials[material] += quantity
        else:
            if material not in junks:
                junks[material] = quantity
            else:
                junks[material] += quantity

    for ore, value in key_materials.items():
        if value >= 250:
            key = True
            if ore == "fragments":
                legendary_item = "Valanyr"
                value -= 250
            elif ore == "shards":
                legendary_item = "Shadowmourne"
                value -= 250
            elif ore == "motes":
                legendary_item = "Dragonwrath"
                value -= 250
            break
    if key:
        break
    materials = input()

print(f"{legendary_item} obtained!")
filtered_items = dict(sorted(key_materials.items(), reverse=True, key=lambda kvp: kvp[1]))
print(filtered_items)