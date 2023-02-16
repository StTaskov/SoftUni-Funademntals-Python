list_of_number_as_string = input().split(", ")
list_of_numbers = [int(numbers) for numbers in list_of_number_as_string]

max_range = 10
min_range = 1
nums_group = []

while max(list_of_numbers)+10> max_range:
    for number in list_of_numbers:
        if number in range(min_range, max_range + 1):
            nums_group.append(number)
            continue
    print(f"Group of {max_range}'s: {nums_group}")
    nums_group.clear()
    max_range += 10
    min_range += 10