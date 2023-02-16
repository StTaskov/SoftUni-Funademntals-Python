n = int(input())
tank = 0

for i in range(1, n +1):
    liters = int(input())

    if tank + liters > 255:
        print("Insufficient capacity!")
    else:
        tank += liters
print(tank)