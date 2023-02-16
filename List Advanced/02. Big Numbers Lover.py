number_like_string = input().split()

number = sorted(number_like_string)
number = number[:: -1]

print("".join(number))

