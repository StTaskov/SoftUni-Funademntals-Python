
number_snowballs = int(input())

highest_snow = -1
highest_time = -1
highest_quality = -1
value = 0

for snowball in range(1, number_snowballs+1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality

    if snowball_value > value:
        value = snowball_value
        highest_snow = snowball_snow
        highest_time = snowball_time
        highest_quality = snowball_quality
print(f"{highest_snow} : {highest_time} = {int(value)} ({highest_quality})")

