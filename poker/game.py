from deck import deck
from start import players, start_game, Player
from hand import deal_hands
from community import burn_card, burn_cards, flop, flop_cards, turn, turn_cards, river, river_cards
from actions import SmallBlind, BigBlind, Check, Raise, Fold, Call
from betting import Action, TableAction
import time

def new_game():

    players = start_game()

    for player in players:
        if player.position == 2:
            time.sleep(1)
            SmallBlind(player)

        if player.position == 3:
            time.sleep(1)
            BigBlind(player)

    time.sleep(1)
    hands = deal_hands(players)

    TableAction(players)

    flop()
    print(flop_cards)

    TableAction(players)

    turn()
    print(turn_cards)

    TableAction(players)

    river()
    print(river_cards)

    TableAction(players)

new_game()