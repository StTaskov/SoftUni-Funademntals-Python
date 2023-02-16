import re
string_pattern = r"(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-_][A-Za-z]+)+))(\b|(?=\s))"
text = input()
find = [el.group() for el in re.finditer(string_pattern, text)]
print("\n".join(find))
