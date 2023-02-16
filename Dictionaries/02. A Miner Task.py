resource = input()
miner_dict = {}

while not resource == "stop":
    quantity = int(input())
    if resource not in miner_dict:
        miner_dict[resource] = quantity
    else:
        miner_dict[resource] += quantity
    resource = input()

for every_key in miner_dict:
    print(f"{every_key} -> {miner_dict[every_key]}")