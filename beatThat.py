import random

def rollDice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    if roll1 == roll2:
        return roll1 * 10 + roll2
    else:
        highestRoll = max(roll1, roll2)
        lowestRoll = min(roll1, roll2)
        return highestRoll * 10 + lowestRoll

def swap(currentPlayer):
    if currentPlayer == 1:
        return 2
    else:
        return 1

def round(currentPlayer):

    print(f"\nPlayer {currentPlayer} starts")
    highest = rollDice()
    print(f"Player {currentPlayer} rolled {highest}")

    currentPlayer = swap(currentPlayer)
    new = rollDice()
    print(f"Player {currentPlayer} rolled {new}")
    
    while new > highest:
        highest = new
        currentPlayer = swap(currentPlayer)
        new = rollDice()
        print(f"Player {currentPlayer} rolled {new}")

    if new == highest:
        print("It's a tie! No points awarded this round.")
        return "0", highest
    
    currentPlayer = swap(currentPlayer)
    print(f"Player {currentPlayer} wins the round!")
    return currentPlayer, highest

def main():
    player1tot = 0
    player2tot = 0
    currentPlayer = 1

    while player1tot < 100 and player2tot < 100:
        currentPlayer, score = round(currentPlayer)
        
        if currentPlayer == 1:
            player1tot += score
            print(f"Player 1 total: {player1tot}")
            print(f"Player 2 total: {player2tot}")
        else:
            player2tot += score
            print(f"Player 1 total: {player1tot}")
            print(f"Player 2 total: {player2tot}")

        currentPlayer = swap(currentPlayer)

    if player1tot >= 100:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

main()