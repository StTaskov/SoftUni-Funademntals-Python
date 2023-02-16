n = int(input())

even = []
odd = []
negative = []
positive = []

for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    if not number % 2 == 0:
        odd.append(number)
    if number < 0:
        negative.append(number)
    if number >= 0:
        positive.append(number)

command = input()

if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
elif command == "positive":
    print(positive)