def calculate_factorial(num_1, num_2):
    result_one = 0
    result_two = 0
    for numbers in range(num_1):
        if numbers == 0:
            result_one += num_1
        else:
            result_one *= num_1 - numbers
    for number in range(num_2):
        if number == 0:
            result_two += num_2
        else:
            result_two *= num_2 - number
    return f"{result_one / result_two:.2f}"


number_one = int(input())
number_two = int(input())

print(calculate_factorial(number_one, number_two))
