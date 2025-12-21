from deck import deck

burn_cards = []

def burn_card():

    burn_cards.append(deck.pop())

flop_cards = []

def flop():

    burn_card()
    flop_cards.append(deck.pop())
    flop_cards.append(deck.pop())
    flop_cards.append(deck.pop())

turn_cards = []

def turn():

    burn_card()
    turn_cards.append(deck.pop())

river_cards = []

def river():

    burn_card()
    river_cards.append(deck.pop())

