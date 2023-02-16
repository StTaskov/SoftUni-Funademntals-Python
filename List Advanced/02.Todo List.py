command = input()
todo_notes = [0] * 10

while not command == "End":
    token = command.split("-")
    importance = int(token[0]) - 1
    to_make = token[1]
    todo_notes[importance] = to_make
    command = input()

notes = [el for el in todo_notes if not el == 0]

print(notes)
