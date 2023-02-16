HIGH_FIRE = range(81, 126)
MEDIUM_FIRE = range(51, 81)
LOW_FIRE = range(1, 51)

fire = input().split("#")
water = int(input())

effort = 0
put_out_of_fire = []

for elements in fire:
    type_of_fire, value = elements.split(" = ")
    value = int(value)

    if type_of_fire == "High" and value not in HIGH_FIRE:
        continue
    elif type_of_fire == "Medium" and value not in MEDIUM_FIRE:
        continue
    elif type_of_fire == "Low" and value not in LOW_FIRE:
        continue
    else:
        if water >= value:
            water -= value
            effort += value * 0.25
            put_out_of_fire.append(value)
        else:
            continue
print("Cells:")
for value in put_out_of_fire:
    print(f" - {value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_of_fire)}")
