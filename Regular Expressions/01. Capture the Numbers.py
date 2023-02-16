import re

text = input()
pattern = r"\d+"
numbers = []

while not text == "":
    find = re.findall(pattern, text)
    numbers.extend(find)
    text = input()

print(*numbers)

