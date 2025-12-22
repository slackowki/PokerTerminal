def display_cards(card1, card2, card3=None, card4=None, card5=None):

    cards = [card1, card2, card3, card4, card5]
    cards = [c for c in cards if c is not None]
    cards_ranks = []
    cards_suits = []

    for card in cards:

        suit_icons = {'Clubs': '♣', 'Spades': '♠', 'Diamonds': '♦', 'Hearts': '♥'}
        suit_icon = suit_icons[card.suit]
        face_icons = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

        if card.rank > 10:
            number_displayed = face_icons[card.rank]
        else:
            number_displayed = card.rank

        cards_ranks.append(number_displayed)
        cards_suits.append(suit_icon)

    top =    " ".join(["┌─────┐" for c in cards])
    rank1 =  " ".join([f"│ {cards_ranks[i]:<2}  │" for i in range(len(cards))])
    suit =   " ".join([f"│  {cards_suits[i]}  │" for i in range(len(cards))])
    rank2 =  " ".join([f"│  {cards_ranks[i]:>2} │" for i in range(len(cards))])
    bottom = " ".join(["└─────┘" for c in cards])

    print(f"{top}\n{rank1}\n{suit}\n{rank2}\n{bottom}")