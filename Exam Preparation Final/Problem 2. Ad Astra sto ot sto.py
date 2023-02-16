import re
total_calories = 0
pattern = r"(\||#)(?P<food>[a-zA-Z\s?]+)\1(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>\d+)\1"
text = input()

find = [el.groupdict() for el in re.finditer(pattern, text)]
for every_element in find:
    every_element["calories"] = int(every_element["calories"])
    total_calories += every_element["calories"]

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for ele in find:
    print(f"Item: {ele['food']}, Best before: {ele['date']}, Nutrition: {ele['calories']}")