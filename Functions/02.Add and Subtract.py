def add_and_subtract(n_1, n_2, n_3):

    def sum_numbers(num_1, num_2):
        result = num_1 + num_2
        return result

    def subtract(num_3):
        result_2 = sum_numbers(n_1, n_2) - num_3
        return result_2
    return subtract(n_3)


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(add_and_subtract(number_one, number_two, number_three))
