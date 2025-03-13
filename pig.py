import random

def rollDice():
    return random.randint(1,6)

def Pig():
    def playerTurnPig(player):
        turnTot = 0
        while True:            # Icky, but necessary for this code 
            roll = rollDice()
            print(f"{player} rolled a {roll}")
            if roll == 1:
                print(f"{player} rolled a 1! Turn over, no points added.")
                return 0
            else:
                turnTot += roll
                print(f"{player}'s turn total is now {turnTot}")
                hold = input(f"{player}, do you want to hold? (y/n): ").lower()
                if hold == 'y':
                    return turnTot

    player1Score = 0
    player2Score = 0

    while player1Score < 100 and player2Score < 100:
        print("\nPlayer 1's turn")
        player1Score += playerTurnPig("Player 1")
        print(f"Player 1's total score is {player1Score}")

        if player1Score >= 100:
            print("Player 1 wins!")
            break

        print("\nPlayer 2's turn")
        player2Score += playerTurnPig("Player 2")
        print(f"Player 2's total score is {player2Score}")

        if player2Score >= 100:
            print("Player 2 wins!")
            break
Pig()


            