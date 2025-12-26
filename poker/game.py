from deck import deck
from start import players, start_game, Player
from hand import deal_hands
from community import burn_card, burn_cards, flop, flop_cards, turn, turn_cards, river, river_cards
from actions import SmallBlind, BigBlind, Check, Raise, Fold, Call
from betting import Action, TableAction
import time

def new_game():

    # Rounds include pre-flop (0), flop (1), turn (2), and river (3).
    round = 0

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

    TableAction(players, round=0)

    flop()
    print(flop_cards)

    TableAction(players, round=1)

    turn()
    print(turn_cards)

    TableAction(players, round=2)

    river()
    print(river_cards)

    TableAction(players, round=3)

new_game()