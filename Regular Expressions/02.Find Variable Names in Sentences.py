import re

text = input()
pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"
find = [el.group() for el in re.finditer(pattern, text)]

print(",".join(find))
