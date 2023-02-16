first_list = input().split(", ")
second_list = input().split(", ")


new_list = [element for element in first_list if any(element) in second_list]

# for el in first_list:
#     for word in second_list:
#         if el in word:
#             if el in new_list:
#                 continue
#             else:
#                 new_list.append(el)
print(new_list)
