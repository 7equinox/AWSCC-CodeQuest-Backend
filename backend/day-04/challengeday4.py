
def funct_rock_paper_scissors_game():
    str_player1 = input("Player 1: ")
    str_player2 = input("Player 2: ")

    if (str_player1.lower()) == "rock" and (str_player2.lower()) == "scissors":
        print("\nPlayer1 Wins!")
    elif (str_player1.lower()) == "rock" and (str_player2.lower()) == "paper":
        print("\nPlayer2 Wins!")
    elif (str_player1.lower()) == "scissors" and (str_player2.lower()) == "rock":
        print("\nPlayer2 Wins!")
    elif (str_player1.lower()) == "scissors" and (str_player2.lower()) == "paper":
        print("\nPlayer1 Wins!")
    elif (str_player1.lower()) == "paper" and (str_player2.lower()) == "rock":
        print("\nPlayer1 Wins!")
    elif (str_player1.lower()) == "paper" and (str_player2.lower()) == "scissors":
        print("\nPlayer2 Wins!")
    elif (str_player1.lower() == str_player2.lower()):
        print("\nIt's a tie!")
    else:
        print("Invalid input. Please try again.\n")
        funct_rock_paper_scissors_game()
    
    
if __name__ == "__main__":
    print("Rock-Paper-Scissors Game\n")
    funct_rock_paper_scissors_game()