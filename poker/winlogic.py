from community import flop_cards, turn_cards, river_cards
from actions import GetActivePlayers
from start import players
from hand import hands

community_cards = flop_cards + turn_cards + river_cards

still_in_hand = GetActivePlayers(players)

def CompareHands(flop_cards, turn_card, river_card, players=still_in_hand):

    # Evaluates hands

def Flush(player, card1, card2, flop_cards, turn_cards, river_cards):

    hasFlush = False
    playerBestFlush = None

    all_cards = [card1, card2] + flop_cards + turn_cards + river_cards

    clubs_count = []
    spades_count = []
    diamonds_count = []
    hearts_count = []

    for card in all_cards:
        if card.suit == 'Clubs':
            clubs_count.append(card)
        if card.suit == 'Spades':
            spades_count.append(card)
        if card.suit == 'Diamonds':
            diamonds_count.append(card)
        if card.suit == 'Hearts':
            hearts_count.append(card)

    mostSuits = max(clubs_count, spades_count, diamonds_count, hearts_count, key=len)

    if len(mostSuits) > 4:
        hasFlush = True
        mostSuits = sorted(mostSuits, key=lambda card: card.value, reverse=True)
        playerBestFlush = mostSuits[:5]

    return hasFlush, playerBestFlush


    



    player_card_1 = hands[player.name][0]
    player_card_2 = hands[player.name][1]



