from start import players
from actions import SmallBlind, BigBlind, Check, Raise, Fold, Call, table_bet, Win, ClearGame

def Action(player):

    while True:
        action = int(input(
                f"\n{player.name}'s turn!"
                "\nChoose from the following options:"
                "\n1 for Check"
                "\n2 for Raise"
                "\n3 for Fold"
                "\n4 for Call"
                "\nWhat option do you choose? : "
            ))

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

