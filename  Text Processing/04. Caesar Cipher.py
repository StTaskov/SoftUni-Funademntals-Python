text = input()

new_text = ""

for every_char in text:
    new_char = chr(ord(every_char) + 3)
    new_text += new_char
print(new_text)
