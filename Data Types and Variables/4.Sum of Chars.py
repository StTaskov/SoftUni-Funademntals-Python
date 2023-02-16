n = int(input())


sum = 0

for i in range(1, n+1):
    latin_letters = input()
    letter_like_num = ord(latin_letters)
    sum += letter_like_num
print(f"The sum equals: {sum}")

