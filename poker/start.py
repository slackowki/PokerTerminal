from dataclasses import dataclass

@dataclass
class Player:
    name: str
    position: int
    balance: int
    folded: bool = False
    current_bet: int = 0

players = []

def start_game():

    player_count = 0

    player_count = int(input("How many players? : "))

    while player_count < 3:
        player_count = int(input("How many players? : "))
        if player_count < 3:
            print("Not enough players! Need at least 3.")

    # Names
    for i in range(1, ((player_count)+1)):

        name = input(f"What's player {i}'s name? : ")
        position = i
        balance = int(input(f"What's player {i}'s balance? : "))

        new_player = Player(name, position, balance)
        players.append(new_player)

    #print(players)
    return players

#start_game()
    
