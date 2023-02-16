def sum_of_eben_and_odd(num1):
    num1 = str(num1)
    sum_for_even = 0
    sum_for_odd = 0
    for elements in num1:
        elements = int(elements)
        if elements % 2 == 0:
            sum_for_even += elements
        else:
            sum_for_odd += elements
    return [sum_for_odd, sum_for_even]


number = int(input())
result = sum_of_eben_and_odd(number)
sum_of_odd = result[0]
sum_of_even = result[1]

print(f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}")
