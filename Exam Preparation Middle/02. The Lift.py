waiting_people = int(input())
lift_state = [int(el) for el in input().split()]

capacity_of_wagon = 4

for index in range(len(lift_state)):
    diff = capacity_of_wagon - lift_state[index]
    if waiting_people >= capacity_of_wagon:
        lift_state[index] = capacity_of_wagon
        waiting_people -= diff
    else:
        lift_state[index] = waiting_people
        waiting_people -= waiting_people

abc = [cart for cart in lift_state if cart < 4]
if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(" ".join([str(el) for el in lift_state]))
elif len(abc) > 0:
    print("The lift has empty spots!")
    print(" ".join([str(el) for el in lift_state]))
else:
    print(" ".join([str(cart) for cart in lift_state]))
