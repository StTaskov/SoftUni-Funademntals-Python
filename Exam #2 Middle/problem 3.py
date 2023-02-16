price = [int(el) for el in input().split()]
entry_point = int(input())
type_of_items = input()
left_sum = []
right_sum = []
position = ""


for items in range(0, len(price)-1, 2):
    left_sum.append(price[items])
    if items + 1 == entry_point:
        continue
    right_sum.append(price[items+1])

if sum(left_sum) >= sum(right_sum):
    position = "Left"
    print(f"{position} - {str(sum(left_sum))}")
else:
    position = "Right"
    print(f"{position} - {str(sum(right_sum))}")

