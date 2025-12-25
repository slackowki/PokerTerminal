from deck import deck
from prints import *
import random
import time

def deal_hands(players):

    hands = {}

    random.shuffle(deck)

    for player in players:
        hands[player.name] = []

    for player in players:
        hands[player.name].append(deck.pop())

    for player in players:
        hands[player.name].append(deck.pop())

        while True:

            reveal_hand = int(input(f"\n{player.name}, enter 1 to see your hand : "))

            if reveal_hand == 1:
                
                display_cards(hands[player.name][0], hands[player.name][1])
                
                clear_lines(12, 3)

                break

    #print(hands)

    return hands

#players = [Player("Simon", 1), Player("Zoe", 2), Player("Carmel", 3)]
#deal_hands(players)