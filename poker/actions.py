from start import players

pot = 0
table_bet = 20

def SmallBlind(player):
    global pot, table_bet

    amount = (table_bet // 2)
    player.balance -= amount
    player.current_bet += amount
    pot += amount

    return pot, table_bet

def BigBlind(player):
    global pot, table_bet

    player.balance -= table_bet
    player.current_bet += table_bet
    pot += table_bet

def Check(player):

    return table_bet
    

def Raise(player, amount):
    global pot, table_bet

    player.balance -= amount
    player.current_bet += amount
    pot += amount
    table_bet += amount

    return pot, table_bet
    

def Fold(player):

    player.folded = True
    player.current_bet = 0


def Call(player):
    global pot

    amount = table_bet - player.current_bet
    player.balance -= amount
    player.current_bet += amount
    pot += amount

    return pot

def Win(player):
    global pot

    player.balance += pot
    pot = 0
    return


def ClearGame(players):
    global pot, table_bet

    pot = 0
    table_bet = 20

    for player in players:

        player.current_bet = 0
        player.position += 1

        if player.position > len(players):
            player.position = 1