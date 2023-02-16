import re

text = input()
furniture_list = []
sum = 0
pattern = r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+((\.\d+))?)\!(?P<quantity>[0-9]+)"

while not text == "Purchase":
    match = re.match(pattern, text)
    if match:
        data = match.groupdict()
        furniture_list.append(data["name"])
        sum += int(data["quantity"]) * float(data["price"])
    text = input()

print("Bought furniture:")
if furniture_list:
    print("\n".join(furniture_list))
print(f"Total money spend: {sum:.2f}")

