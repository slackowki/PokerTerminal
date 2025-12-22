from deck import deck
from prints import display_cards
import random

def deal_hands(players):

    hands = {}

    random.shuffle(deck)

    for player in players:
        hands[player.name] = []

    for player in players:
        hands[player.name].append(deck.pop())

    for player in players:
        hands[player.name].append(deck.pop())
        print(f"\n{player.name}'s hand:")
        display_cards(hands[player.name][0], hands[player.name][1])

    #print(hands)

    return hands

#players = [Player("Simon", 1), Player("Zoe", 2), Player("Carmel", 3)]
#deal_hands(players)