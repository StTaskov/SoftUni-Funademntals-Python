words = input()
dict_for_chars = {}

for key in words:
    if key == " ":
        continue
    if key not in dict_for_chars:
        dict_for_chars[key] = 1
    else:
        dict_for_chars[key] += 1


for keys in dict_for_chars:
    print(f"{keys} -> {dict_for_chars[keys]}")

