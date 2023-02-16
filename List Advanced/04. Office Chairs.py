n_rooms = int(input())
free_chairs = 0
is_chair_enough = True

for room in range(1, n_rooms+1):
    chairs, people = input().split(" ")
    people = int(people)
    diff = abs(len(chairs) - people)
    free_chairs += diff
    if people > len(chairs):
        print(f"{diff} more chairs needed in room {room}")
        is_chair_enough = False

if is_chair_enough:
    print(f"Game On, {free_chairs} free chairs left")
