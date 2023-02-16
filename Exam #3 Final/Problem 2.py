import re

n = int(input())
counter = 0
pattern = r"(U\$)(?P<username>[A-Z][a-z]{2,})(U\$P@\$)(?P<password>[A-Za-z]{5,}\d+)(P@\$)"

for _ in range(n):
    text = input()
    match = re.match(pattern, text)
    find = re.finditer(pattern, text)
    if match:
        print("Registration was successful")
        for el in find:
            asd = el.groupdict()
            for key in asd.keys():
                print(f"Username: {asd['username']}, Password: {asd['password']}")
                counter += 1
                break
    else:
        print("Invalid username or password")
print(f"Successful registrations: {counter}")


