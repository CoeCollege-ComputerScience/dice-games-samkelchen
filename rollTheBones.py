import random

def rollDice():
    rolls = []
    for i in range(5):
        roll = random.randint(1,6)
        rolls.append(roll)
    tot = sum(rolls)
    return tot, rolls

def bet():
    print("Lets play a game of Roll the Bones!")
    totPoints = 0
    rounds = 0
    while True:
        guess = int(input("\nEnter your guess: "))
        while not(5 <= guess <= 30):
            guess = int(input("Enter your guess: "))
        
        tot, rolls = rollDice()
        print(f"You rolled {rolls}, which has a sum of {tot}")
        
        roundPoints = 0
        if guess == tot:
            roundPoints += 50
            print("Yippee! You get 50 points!")
            print(f"Round total: {roundPoints}")
        elif guess < tot:
            roundPoints += (guess - 5)
            print(f"Your guess was too low. You get {guess - 5} points.")
            print(f"Round total: {roundPoints}")
        else:
            roundPoints += (5 - guess)
            print(f"Your guess was too high. You get {5 - guess} points.")
            print(f"Round total: {roundPoints}") 
        
        totPoints += roundPoints
        rounds += 1
        print(f"Total points: {totPoints}")
        print(f"Rounds played: {rounds}")
        print(f"Average points per round: {totPoints / rounds}")
        
        again = input("Do you want to play again? (y/n): ").lower()
        while again not in ['y', 'n']:
            again = input("Do you want to play again? (y/n): ").lower()
        if again == 'n':
            print("Thanks for playing!")
            break

bet()
