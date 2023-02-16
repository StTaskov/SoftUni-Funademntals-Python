words = input().split()

first_word = words[0]
second_word = words[1]
diff = abs(len(first_word) - len(second_word))

total_sum = 0
index = 0

while index < len(first_word):
    if se:
        total_sum += ord(first_word[index]) * ord(second_word[index])
    index += 1
print(total_sum)