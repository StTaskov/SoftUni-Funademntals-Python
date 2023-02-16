ls_like_string = input().split(" ")
count_of_removes = int(input())

new_ls = []

for element in ls_like_string:
    new_ls.append(int(element))
for _ in range(count_of_removes):
    new_ls.remove(min(new_ls))
print(new_ls)
