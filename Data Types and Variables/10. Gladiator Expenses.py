lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

price = 0
shield_brakes = 0

for lost_fight in range(1, lost_fights_count+1):
    if lost_fight % 2 == 0:
        price += helmet_price
    if lost_fight % 3 == 0:
        price += sword_price
    if lost_fight % 6 == 0:
        price += shield_price
        shield_brakes += 1
        if shield_brakes == 2:
            price += armor_price
            shield_brakes = 0

print(f"Gladiator expenses: {price:.2f} aureus")



