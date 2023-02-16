first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
people_count = int(input())

time = 0

while people_count > 0:
    all_employee_efficiency = first_employee + second_employee + third_employee
    people_count -= all_employee_efficiency
    time += 1
    if time % 4 == 0:
        time += 1
print(f"Time needed: {time}h.")