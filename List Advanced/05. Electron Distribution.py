electrons = int(input())
list_of_shells = []
current_shell = 1

while electrons > 0:
    current_shell_capacity = 2*current_shell**2
    if current_shell_capacity > electrons:
        list_of_shells.append(electrons)
    else:
        list_of_shells.append(current_shell_capacity)
    electrons -= current_shell_capacity
    current_shell += 1

print(list_of_shells)