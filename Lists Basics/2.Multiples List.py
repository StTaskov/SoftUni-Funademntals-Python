factor = int(input())
count = int(input())

li = []

for i in range(1, count+1):
    element = i * factor
    li.append(element)

print(li)
