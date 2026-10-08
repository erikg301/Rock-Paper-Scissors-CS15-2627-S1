import random

# rock paper scissors

def get_cpu_choice():
    cpu_choice = random.choice(["rock", "paper", "scissors"])
    return cpu_choice

def get_player_choice():
    while True:
        player_choice = input("Rock, paper, or scissors?\n")
        player_choice = player_choice.lower()
        # only let them leave the loop if its valid
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
        # cpu picked scissors
        if player_choice == "paper":
            winner = "CPU"
        else:
            winner = "PLAYER"
    return winner

cpu_choice = get_cpu_choice()

player_choice = get_player_choice()

winner = check_winner(cpu_choice, player_choice)

print("CPU chose " + cpu_choice)
print("Player chose " + player_choice)
print("Winner: " + winner)