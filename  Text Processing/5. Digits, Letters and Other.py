text = input()
nums = ""
letters = ""
characters = ""

for chars in text:
    if chars.isdigit():
        nums += chars
    elif chars.isalpha():
        letters += chars
    else:
        characters += chars

print(nums)
print(letters)
print(characters)
