player1 = input("Player 1, enter rock, paper, or scissors: ").lower()
player2 = input("Player 2, enter rock, paper, or scissors: ").lower()
choices = ["rock", "paper", "scissors"]
if player1 in choices and player2 in choices:
    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
else:
    print("Invalid input! Please enter rock, paper, or scissors.")