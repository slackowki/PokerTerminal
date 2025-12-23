from start import players
from prints import *
import time

pot = 0
table_bet = 20

def SmallBlind(player):
    global pot, table_bet

    amount = (table_bet // 2)
    player.balance -= amount
    player.current_bet += amount
    pot += amount

    print(f"{BOLD}{BLUE}{player.name}{RESET}{BOLD} is the small blind!")

    return pot, table_bet

def BigBlind(player):
    global pot, table_bet

    player.balance -= table_bet
    player.current_bet += table_bet
    pot += table_bet

    print(f"{BOLD}{BLUE}{player.name}{RESET}{BOLD} is the big blind!{RESET}\n")

    return pot, table_bet

def CurrentStatus(players):
    global pot, table_bet

    still_in_hand = []

    for player in players:

        if player.folded == False:
            still_in_hand.append(player.name)

    still_in_hand_count = len(still_in_hand)

    print(f"There are {BOLD}{RED}{still_in_hand_count}{RESET} players in.\n")
    time.sleep(1)
    print(f"The players left are: {', '.join(still_in_hand)}.\n")
    time.sleep(1)
    print(f"{BOLD}The pot is up to {RED}${pot}!{RESET}\n")
    time.sleep(1)

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