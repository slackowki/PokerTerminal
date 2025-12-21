from collections import namedtuple

Card = namedtuple('Card', ['suit', 'rank'])

deck = []

suits = ["Clubs", "Spades", "Diamonds", "Hearts"]

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for rank in ranks:
    for suit in suits:
        deck.append(Card(suit, rank))
