import sys
command = input()
coffee_counter = 0

while not command == "END":
    if command.isupper() == True:
        if command == "CODING" or "DOG" or "CAT" or "MOVIE":
            coffee_counter += 2
    elif command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_counter += 1
        command = input()
    if coffee_counter == 5:
        print("You need extra sleep")
        sys.exit()


print(coffee_counter)

