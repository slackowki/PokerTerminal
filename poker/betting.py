from start import players
from actions import SmallBlind, BigBlind, Check, Raise, Fold, Call, table_bet, Win, ClearGame, CurrentStatus
from prints import *
import questionary
from questionary import Style

custom_style = Style([
    ('question', 'bold'),
    ('highlighted', 'fg:green bold'),
    ('pointer', 'fg:green bold'),
])

def get_player_action(player):

    options = ["Check", "Raise", "Fold", "Call"]

    question = f"""

Player Turn: {player.name}
Balance: ${player.balance}
Your Bet: ${player.current_bet}
Table Bet: ${table_bet}

Choose your action:"""
    
    option = questionary.select(
        question,
        choices=options,
        style=custom_style,
        pointer="►"
    ).ask()

    index = options.index(option)
    return index + 1


def Action(player):

    while True:

        CurrentStatus(players)

        print(f"Balance: {BOLD}{GREEN}${player.balance}{RESET}\n")
        print(f"Current Bet: {BOLD}{YELLOW}${player.current_bet}{RESET}\n")
        print(f"Table Bet: {BOLD}{RED}${table_bet}{RESET}\n")

        if player.current_bet < table_bet:
            raise_amount = table_bet - player.current_bet
            print(f"You need to add {BOLD}{RED}${raise_amount}{RESET} to stay in!\n")

        action = get_player_action(player)

        if action == 1:

            if player.current_bet == table_bet:
                Check(player)
                break

            else:
                print(f"Someone has raised the table bet to {table_bet}!")
                continue

        elif action == 2:

            amount = int(input("How much would you like to raise? : "))

            if player.balance >= amount:
                Raise(player, amount)
                break

            else:
                print(f"You do not have the funds to raise it to {amount}. You only have {player.balance} remaining.")
                continue

        elif action == 3:

            Fold(player)
            break

        elif action == 4:

            if player.balance >= table_bet - player.current_bet:
                Call(player)
                break

            else:
                print(f"You do not have the funds to call!")
                # Later, add side-pots logic here.
                continue

def TableAction(players):

    sorted_players = sorted(players, key=lambda p: p.position)
    action_order = sorted_players[1:] + sorted_players[:1]

    while True:

        for player in action_order:

            if player.folded:
                continue

            Action(player)

        active_players = [p for p in players if not p.folded]

        if len(active_players) == 1:

            Win(active_players[0])
            ClearGame(players)
            return

        bets = [p.current_bet for p in active_players]

        if len(set(bets)) == 1:
            break

