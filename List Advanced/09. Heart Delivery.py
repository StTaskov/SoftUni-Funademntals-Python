def if_successful(lst):
    if all([v == 0 for v in lst]):
        return True
    return False


hearths = [int(number_of_hearths) for number_of_hearths in input().split("@")]
command = input()
cupid_last_position = 0

while not command == "Love!":
    command, length_of_jump = command.split()
    length_of_jump = int(length_of_jump)
    for house_index in range(0 + length_of_jump, len(hearths), length_of_jump):
        if hearths[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
        hearths[house_index] -= 2
        if hearths[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")
            continue
        if length_of_jump > len(hearths):
            continue
        cupid_last_position = house_index
        continue

    command = input()

print(f"Cupid's last position was {cupid_last_position}.")
if if_successful(hearths):
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {hearths.count([el for el in hearths if not el == 0 ])} places.")
