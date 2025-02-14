import random


def play_game(rounds):
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    for i in range(rounds):
        player_choice = input("Select a choice from these: (rock, paper, scissors)")
        if player_choice not in choices:
            print("Choice not found, please choose select again")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer chose:{computer_choice} ")

# GAMEPLAY

        if player_choice == computer_choice:
            print("it is a tie for this round")

        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'scissors' and computer_choice == 'paper') or \
            (player_choice == 'paper' and computer_choice == 'scissors'):
            print("You win this round")
            player_score += 1
        else:
            print("You lose this round")
            computer_score += 1

# CHECK FOR WINNER
        
        if player_score == (rounds // 2) +1 :
            print("You are the winner of the game")
            return
        elif computer_score == (rounds // 2) + 1 :
            print("Computer has won")
            return
    print(f"Final Score - You {player_score}, Computer {computer_score}")

def main():
    rounds = int(input("Select the number of rounds to play, (3 or 5)"))
    if rounds in [3, 5]:
        play_game(rounds)
    else:
        print("Invalid! Please select 3 or 5")

if __name__ == "__main__": 
    main()



