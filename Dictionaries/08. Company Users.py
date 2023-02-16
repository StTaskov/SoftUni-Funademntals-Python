data = input()

company_dict = {}

while not data == "End":
    company_name, i_d = data.split(" -> ")
    if company_name not in company_dict:
        company_dict[company_name] = []
    if i_d not in company_dict[company_name]:
        company_dict[company_name].append(i_d)
    else:
        pass

    data = input()

filtered_data = dict(sorted(company_dict.items(), key=lambda kvp: kvp[0]))

for key, value in filtered_data.items():
    print(key)
    for el in value:
        print(f"-- {''.join(el)}")