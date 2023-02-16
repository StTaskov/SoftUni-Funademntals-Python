energy = int(input())

won_battles = 0

distance = input()
u_win = True
while not distance == "End of battle":
    distance = int(distance)
    energy -= distance
    won_battles += 1
    if won_battles % 3 == 0:
        energy += won_battles
    if energy < distance:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        u_win = False
        break
    distance = input()

if u_win:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
