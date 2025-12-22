from deck import deck
from start import players, start_game, Player
from hand import deal_hands
from community import burn_card, burn_cards, flop, flop_cards, turn, turn_cards, river, river_cards
from actions import SmallBlind, BigBlind, Check, Raise, Fold, Call
from betting import Action, TableAction

def new_game():

    players = start_game()

    for player in players:
        if player.position == 2:
            SmallBlind(player)

        if player.position == 3:
            BigBlind(player)

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