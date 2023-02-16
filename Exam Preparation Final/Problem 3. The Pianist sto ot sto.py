def is_it_exist(dct, pies):
    if pies in dct:
        return True
    return False


number_of_pieces = int(input())

pieces_dict = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces_dict[piece] = {"composer": composer, "key": key}

command = input()

while not command == "Stop":
    command = command.split("|")
    if command[0] == "Add":
        piesa = command[1]
        compositor = command[2]
        kluch = command[3]
        if is_it_exist(pieces_dict, piesa):
            print(f"{piesa} is already in the collection!")
        else:
            pieces_dict[piesa] = {"composer": compositor, "key": kluch}
            print(f"{piesa} by {compositor} in {kluch} added to the collection!")
    elif command[0] == "Remove":
        piesa = command[1]
        if is_it_exist(pieces_dict, piesa):
            pieces_dict.pop(piesa)
            print(f"Successfully removed {piesa}!")
        else:
            print(f"Invalid operation! {piesa} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piesa = command[1]
        new_key = command[2]
        if is_it_exist(pieces_dict, piesa):
            pieces_dict[piesa]["key"] = new_key
            print(f"Changed the key of {piesa} to {new_key}!")
        else:
            print(f"Invalid operation! {piesa} does not exist in the collection.")
    command = input()

current_dict = sorted(pieces_dict.items(), key=lambda kvp: kvp[0], reverse=False)

for el in current_dict:
    piece = el[0]
    composer = el[1]['composer']
    key = el[1]['key']
    print(f'{piece} -> Composer: {composer}, Key: {key}')