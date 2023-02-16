list_of_str = input().split()

result = ""
for word in list_of_str:
    result += word * len(word)

print(result)
