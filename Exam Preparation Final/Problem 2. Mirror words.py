import re


text = input()
mirror_words = []

pattern = r"(@|#)(?P<word_one>([A-Za-z]{3,}))\1\1(?P<word_two>([A-Za-z]{3,}))\1"

find = [el.groupdict() for el in re.finditer(pattern, text)]

for index in range(len(find)):
    if len(find[index]["word_one"]) == len(find[index]["word_two"]) and find[index]["word_one"] == find[index]["word_two"][::-1]:
        mirror_words.append(find[index]["word_one"])
        mirror_words.append(find[index]["word_two"])

if not find:
    print("No word pairs found!")
else:
    print(f"{len(find)} word pairs found!")

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    for index in range(0, len(mirror_words), 2):
        if index < len(mirror_words[-1]):
            print(f"{mirror_words[index]} <=> {mirror_words[index+1]}", end=", ")
        else:
            print(f"{mirror_words[index]} <=> {mirror_words[index + 1]}")
