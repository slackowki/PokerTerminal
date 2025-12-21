from deck import deck
import random

def deal_hands(players):
    random.shuffle(deck)

    hands = {}

    for player in players:
        hands[player.name] = []

    for player in players:
        hands[player.name].append(deck.pop())

    for player in players:
        hands[player.name].append(deck.pop())

    print(hands)

    return hands

#players = [Player("Simon", 1), Player("Zoe", 2), Player("Carmel", 3)]
#deal_hands(players)