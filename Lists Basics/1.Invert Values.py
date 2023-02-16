string = input()

li = string.split()
li_2 = []

for first_element in li:

    if int(first_element) > 0:
            li_2.append(-int(first_element))
    elif int(first_element) == 0:
            li_2.append(0)
    elif int(first_element) < 0:
            li_2.append(abs(int(first_element)))

print(li_2)
