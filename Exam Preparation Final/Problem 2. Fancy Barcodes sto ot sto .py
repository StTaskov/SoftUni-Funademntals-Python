import re

n = int(input())
pattern = r"@#+([A-Z][A-Za-z0-9]{5,}[A-Z])@#+"

valid_barcodes = []
invalid_barcodes = []
product_group_lie_string = ""
product_group = ""

for _ in range(n):
    bar_code = input()
    match = re.match(pattern, bar_code)
    if match:
        valid_barcodes.append(match.group())
    else:
        invalid_barcodes.append(bar_code)

