from random import randint, choice

print("Let's play some Rock-Paper-Scissors!")

player_count = randint(2,10)
players = []
POSSIBLE_MOVES = ["rock", "paper", "scissors"]

class Player:
    def __init__(self, name):
        self.name = name
        self.move = None

def losing_move(winning_move):
    if winning_move == "rock":
        return "scissors"
    elif winning_move == "scissors":
        return "paper"
    else:
        return "rock"

def eliminated_players(winning_move, results):
    starting_total = player_count
    for player in players:
        if player.move == losing_move(winning_move):
            players.remove(player)
    return (f"Eliminated {starting_total - player_count} players")
    

# Create Player instances and assign names
for i in range(0, player_count):
    players.append(Player(f"Player {i + 1}"))

while len(players) > 1:


    # Assign player moves:

    for player in players:
        player.move = choice(POSSIBLE_MOVES)

    # Count moves to determine winning move

    results_for_round = []
    results_count = {}
    for player in players:
        results_for_round.append(player.move)

    for result in results_for_round:\
        results_count[result] = results_for_round.count(result)

    winning_move = max(results_count, key=results_count.get) # Needs guard clause against ties

    # Determine number of unique moves
    unique_moves = set(results_for_round)

    # For each remaining player, display ID and move
    for player in players: 
        print(f"{player.name} threw {player.move}")

    # Compare winning moves to other moves to eliminate players
    if len(unique_moves) == 1:

        print("It's a tie!")
    elif len(unique_moves) == 2:
        print(eliminated_players(winning_move, results)
    elif len(unique_moves) == 3 # with no tie for winner :
        print(eliminated_players(winning_move, results)

    else:
        print("Three moves and a tie! No one eliminated.")


# Display winner
print(f"{players[0]} is the winner!")