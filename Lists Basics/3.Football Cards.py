cards = input()

cards_like_string = cards.split()
ls_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
ls_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

for elements in ls_A:
    if elements in cards_like_string:
        if elements in ls_A:
            ls_A.remove(elements)
counter_for_teamA = len(ls_A)

for element in ls_B:
    if element in cards_like_string:
        if element in ls_B:
            ls_B.remove(element)
counter_for_teamB = len(ls_B)


if counter_for_teamA <= 7:
    print(f"Team A - {counter_for_teamA}; Team B - {counter_for_teamB}")
    print("Game was terminated")
elif counter_for_teamB <= 7:
    print(f"Team A - {counter_for_teamA}; Team B - {counter_for_teamB}")
    print("Game was terminated")
else:
    print(f"Team A - {counter_for_teamA}; Team B - {counter_for_teamB}")
