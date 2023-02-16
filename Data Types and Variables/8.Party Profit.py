party_size = int(input())
days = int(input())

coins = 0

for days in range(1, days+1):
    if days % 10 == 0:
        party_size -= 2
    if days % 15 == 0:
        party_size += 5
    coins += 50 - (2 * party_size)
    if days % 3 == 0:
        coins -= 3 * party_size
    if days % 5 == 0:
        coins += 20 * party_size
        if days % 5 == 0 and days % 3 == 0:
            coins -= 2 * party_size

print(f"{party_size} companions received {coins//party_size} coins each.")