import re
text = input().lower()
pattern = f"\\b{input().lower()}\\b"

find = re.findall(pattern, text)
print(len(find))
