words = input().split()
searched_palindrome = input()

found = [el for el in words if el == el[::-1]]

print(found)
print(f"Found palindrome {found.count(searched_palindrome)} times")
