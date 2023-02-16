text = input()

strength = 0

for index in range(len(text)):

    if text[index] == ">":
        strength = int(text[index + 1])
        text_to_replace = range(index+1, strength)
        text.replace(text_to_replace, "")

