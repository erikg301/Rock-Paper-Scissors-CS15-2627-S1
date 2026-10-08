import random

# rock paper scissors
# first to 3 wins

def get_cpu_choice():
    choices = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(choices)
    return cpu_choice


def get_player_choice():
    while True:
        player_choice = input("Rock, paper, or scissors?\n")
        player_choice = player_choice.lower()

        if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
            return player_choice
        else:
            print("Invalid! Type rock, paper, or scissors")


def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
        winner = "Tie"
    elif cpu_choice == "rock":
        if player_choice == "paper":
            winner = "PLAYER"
        else:
            winner = "CPU"
    elif cpu_choice == "paper":
        if player_choice == "scissors":
            winner = "PLAYER"
        else:
            winner = "CPU"
    else:
        if player_choice == "paper":
            winner = "CPU"
        else:
            winner = "PLAYER"
    return winner


def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()
    winner = check_winner(cpu_choice, player_choice)
    print("CPU chose " + cpu_choice)
    print("You chose " + player_choice)
    return winner


player_wins = 0
cpu_wins = 0
ties = 0

print("Rock Paper Scissors! First to 3 wins!")

while player_wins < 3 and cpu_wins < 3:
    print()
    winner = play_round()

    if winner == "PLAYER":
        player_wins = player_wins + 1
        print("You win this round!")
    elif winner == "CPU":
        cpu_wins = cpu_wins + 1
        print("CPU wins this round!")
    else:
        ties = ties + 1
        print("Tie!")

    print("Player: " + str(player_wins))
    print("CPU: " + str(cpu_wins))
    print("Ties: " + str(ties))

print()
if player_wins == 3:
    print("You won the tournament!")
else:
    print("CPU won the tournament!")