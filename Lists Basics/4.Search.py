n = int(input())
searched_word = input()

all_words = []
finded_words = []

for _ in range(n):
    some_string = input()
    all_words.append(some_string)
    if searched_word in some_string:
        finded_words.append(some_string)

print(all_words)
print(finded_words)