def check_it_is_palindrome(ls_pos_int):
    for elements in ls_pos_int:
        if elements == elements[:: -1]:
            print(True)
        else:
            print(False)
    return ""


positive_integer = input().split(", ")

print(check_it_is_palindrome(positive_integer))
