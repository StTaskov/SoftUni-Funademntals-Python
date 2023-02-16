lst_of_numbers = input().split(", ")
number_of_beggars = int(input())

sum_for_beggars = []
start_index = 0

for each_beggars in range(number_of_beggars):
    current_sum = 0
    for sum in range(start_index, len(lst_of_numbers), number_of_beggars):
        current_sum += int(lst_of_numbers[sum])
    sum_for_beggars.append(current_sum)
    start_index += 1
print(sum_for_beggars)




