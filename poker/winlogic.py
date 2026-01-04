from enum import unique
from community import flop_cards, turn, turn_cards, river_cards
from actions import GetActivePlayers
from deck import *
from start import players
from hand import hands

community_cards = flop_cards + turn_cards + river_cards

still_in_hand = GetActivePlayers(players)

def CompareHands(flop_cards, turn_card, river_card, players=still_in_hand):

    # Evaluates hands

def HighCard(card1, card2, flop_cards, turn_cards, river_cards):

   all_cards = [card1, card2] + flop_cards + turn_cards + river_cards
   sorted_cards = sorted(all_cards, key=lambda card: card.rank, reverse=True)
   hand = sorted_cards[:5]

   return True, hand

def TwoPair(card1, card2, flop_cards, turn_cards, river_cards):

    all_cards = [card1, card2] + flop_cards + turn_cards + river_cards
    sorted_cards = sorted(all_cards, key=lambda card: card.rank, reverse=True)

    card_occurences = {}

    for card in sorted_cards:
        card_occurences = card_occurences.get(card.rank, 0) +1

    sorted_occurences = sorted(card_occurences.items(), key=lambda x: (len(x[1]), x[0]), reverse=True)

    pairs = [cards for rank, cards in sorted_occurences if len(cards) == 2]
    
    if len(pairs) >= 2:
        top_pair = pairs[0][:2]
        bottom_pair = pairs[1][:2]

        used_ranks = {top_pair[0].rank, bottom_pair[0].rank}
        kicker = next(card for card in sorted_cards if card.rank not in used_ranks)

        hand = top_pair + bottom_pair + [kicker]

        return True, hand
    
    return False, []


    

def Straight(card1, card2, flop_cards, turn_cards, river_cards):
    all_cards = [card1, card2] + flop_cards + turn_cards + river_cards
    
    sorted_cards = sorted(all_cards, key=lambda card: card.rank, reverse=True)

    rank_to_card = {}

    for card in sorted_cards:
        if card.rank not in rank_to_card:
            rank_to_card[card.rank] = card

    unique_cards = list(rank_to_card.values())

    if 14 in rank_to_card:
        ace = rank_to_card[14]
        unique_cards.append(Card(ace.suit, 1))

    cards_in_a_row = 1
    straight = [unique_cards[0]]

    for i in range(len(unique_cards) -1):

        if unique_cards[i].rank == (unique_cards[i+1].rank +1):
            cards_in_a_row += 1
            straight.append(unique_cards[i + 1])
            if cards_in_a_row >= 5:
                return True, straight[:5]
        else:
            cards_in_a_row = 1
            straight = [unique_cards[i + 1]]

    return False, []



def Flush(card1, card2, flop_cards, turn_cards, river_cards):
    all_cards = [card1, card2] + flop_cards + turn_cards + river_cards

    sorted_cards = sorted(all_cards, key=lambda card: card.rank, reverse=True)

    clubs_count = []
    spades_count = []
    diamonds_count = []
    hearts_count = []

    for card in sorted_cards:
        if card.suit == 'Clubs':
            clubs_count.append(card)
        elif card.suit == 'Spades':
            spades_count.append(card)
        elif card.suit == 'Diamonds':
            diamonds_count.append(card)
        elif card.suit == 'Hearts':
            hearts_count.append(card)

    mostSuits = max(clubs_count, spades_count, diamonds_count, hearts_count, key=len)

    if len(mostSuits) > 4:
        return True, mostSuits[:5]

    return False, []

def StraightFlush(card1, card2, flop_cards, turn_cards, river_cards):

    def FlushHelper(card1, card2, flop_cards, turn_cards, river_cards):
        all_cards = [card1, card2] + flop_cards + turn_cards + river_cards

        sorted_cards = sorted(all_cards, key=lambda card: card.rank, reverse=True)

        clubs_count = []
        spades_count = []
        diamonds_count = []
        hearts_count = []

        for card in sorted_cards:
            if card.suit == 'Clubs':
                clubs_count.append(card)
            elif card.suit == 'Spades':
                spades_count.append(card)
            elif card.suit == 'Diamonds':
                diamonds_count.append(card)
            elif card.suit == 'Hearts':
                hearts_count.append(card)

        flush_cards = max(clubs_count, spades_count, diamonds_count, hearts_count, key=len)

        if len(flush_cards) > 4:
            return True, flush_cards

        return False, []

    def StraightHelper(flush_cards):
        unique_ranks = sorted(set(card.rank for card in flush_cards), reverse=True)

        if 14 in unique_ranks:
            unique_ranks.append(1)

        cards_in_a_row = 1
        straight = [unique_ranks[0]]

        for i in range(len(unique_ranks) -1):

            if unique_ranks[i] == (unique_ranks[i+1] +1):
                cards_in_a_row += 1
                straight.append(unique_ranks[i + 1])
                if cards_in_a_row >= 5:
                    return True, straight[:5]
            else:
                cards_in_a_row = 1
                straight = [unique_ranks[i + 1]]

        return False, []

    hasFlush, flush = FlushHelper(card1, card2, flop_cards, turn_cards, river_cards)

    if hasFlush == True and len(flush) >= 5:
        hasStraightFlush, straightFlush = StraightHelper(flush)

        if hasStraightFlush == True and len(straightFlush) == 5:
            return True, straightFlush
        else:
            return False, []

    else:
        return False, []

        

    





