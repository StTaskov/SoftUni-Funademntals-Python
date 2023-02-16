import re

pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"

text = input()
cool_threshold = 1
current_cool_threshold = 0
the_coolest_emojys = []

for number in text:
    if number.isdigit():
        cool_threshold *= int(number)
    else:
        continue

matched = [el.group() for el in re.finditer(pattern, text)]


for index in range(len(matched)):
    if matched[index].startswith("::"):
        substring = matched[index][2:-2]
        for char in substring:
            current_cool_threshold += ord(char)
        if current_cool_threshold > cool_threshold:
            the_coolest_emojys.append(matched[index])
            current_cool_threshold = 0
        else:
            current_cool_threshold = 0
    elif matched[index].startswith("**"):
        substring = matched[index][2:-2]
        for char in substring:
            current_cool_threshold += ord(char)
        if current_cool_threshold > cool_threshold:
            the_coolest_emojys.append(matched[index])
            current_cool_threshold = 0
        else:
            current_cool_threshold = 0

print(f"Cool threshold: {cool_threshold}")

print(f"{len(matched)} emojis found in the text. The cool ones are:")
for emojy in the_coolest_emojys:
    print(emojy)

