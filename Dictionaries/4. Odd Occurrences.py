words = [word.lower() for word in input().split()]
dictionary = {}

for every_word in words:
    if every_word not in dictionary:
        dictionary[every_word] = 0
    dictionary[every_word] += 1
for key, value in dictionary.items():
    if not value % 2 == 0:
        print(key, end=" ")


