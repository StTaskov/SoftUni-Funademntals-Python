cards = input().split()
number_of_shuffle = int(input())

bottom_card = cards[-1]
top_card = cards[0]

half_cards = len(cards) // 2

shuffled_cards = []
for shuffles in range(number_of_shuffle):
    left_deck = []
    right_deck = []
    for index in range(1, half_cards):
        left_deck.append(cards[index])
    for index in range(half_cards, len(cards) - 1):
        right_deck.append(cards[index])

    for index in range(len(left_deck)):
        shuffled_cards.append((right_deck[index]))
        shuffled_cards.append(left_deck[index])

    cards = shuffled_cards.copy()
    cards.append(bottom_card)
    cards.insert(0, top_card)
    shuffled_cards = []

print(cards)
