user_names = input().split(", ")

valid_usernames = []
is_correct = False

for ever_user in user_names:
    if 3 <= len(ever_user) <= 16:
        is_correct = True
    else:
        is_correct = False
        continue
    for chars in ever_user:
        if chars.isdigit() or chars.isalpha() or chars is "-" or chars is "_":
            is_correct = True
        else:
            is_correct = False
            break
        if not chars.isdigit() and not chars.isalpha() and chars is not "-" and chars is not "_":
            is_correct = False
            break
        else:
            is_correct = True

    if is_correct:
        valid_usernames.append(ever_user)


for user in valid_usernames:
    print(user)
