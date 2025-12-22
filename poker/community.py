from deck import deck
from prints import display_cards

burn_cards = []

def burn_card():

    burn_cards.append(deck.pop())

flop_cards = []

def flop():

    burn_card()
    flop_cards.append(deck.pop())
    flop_cards.append(deck.pop())
    flop_cards.append(deck.pop())
    display_cards(flop_cards[0], flop_cards[1], flop_cards[2])

turn_cards = []

def turn():

    burn_card()
    turn_cards.append(deck.pop())
    display_cards(flop_cards[0], flop_cards[1], flop_cards[2], turn_cards[0])

river_cards = []

def river():

    burn_card()
    river_cards.append(deck.pop())
    display_cards(flop_cards[0], flop_cards[1], flop_cards[2], turn_cards[0], river_cards[0])

