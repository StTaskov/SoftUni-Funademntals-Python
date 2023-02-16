def check_is_number_perfect(num):
    perfect_dicisors = []
    for nums in range(1, num):
        if num % nums == 0:
            perfect_dicisors.append(nums)

    if sum(perfect_dicisors) == num:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(check_is_number_perfect(number))
