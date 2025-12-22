from collections import namedtuple

Card = namedtuple('Card', ['suit', 'rank'])

deck = []

suits = ["Clubs", "Spades", "Diamonds", "Hearts"]

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for rank in ranks:
    for suit in suits:
        deck.append(Card(suit, rank))


def display_card(card):

    suit_icons = {'Clubs': '♣', 'Spades': '♠', 'Diamonds': '♦', 'Hearts': '♥'}
    suit_icon = suit_icons[card.suit]
    face_icons = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

    if card.rank > 10:
        number_displayed = face_icons[card.rank]
    else:
        number_displayed = card.rank

    print(
        f"┌─────┐\n"
        f"│ {number_displayed:<2}  │\n"
        f"│  {suit_icon}  │\n"
        f"│  {number_displayed:>2} │\n"
        f"└─────┘"
    )

#display_card(deck[1])
