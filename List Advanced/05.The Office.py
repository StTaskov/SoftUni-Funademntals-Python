happiness_by_person = input().split()
happiness_factor = int(input())

happiness_like_num = list(map(lambda x: int(x), happiness_by_person))
multiplying_happiness = [num*happiness_factor for num in happiness_like_num]

average = sum(happiness_like_num) // len(happiness_by_person)

filtered = list(filter(lambda x: x > average, multiplying_happiness))

if len(filtered) >= len(multiplying_happiness) / 2:
    print(f"Score: {len(filtered)}/{len(multiplying_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(multiplying_happiness)}. Employees are not happy!")