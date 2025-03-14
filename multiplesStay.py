import random


def rollDice():
    rolls = []
    for i in range(10):
        roll = random.randint(1, 6)
        rolls.append(roll)
    return rolls


def countOutcomes(rolls):           # copilot helped me with this part
    outcome_counts = {}
    for roll in rolls:
        if roll in outcome_counts:
            outcome_counts[roll] += 1
        else:
            outcome_counts[roll] = 1
    return outcome_counts


def selectOutcome(outcome_counts):
    for outcome, count in outcome_counts.items():
        if count > 1:
            return outcome
    return None


def removeOutcome(rolls, outcome):
    new_rolls = []
    for roll in rolls:
        if roll != outcome:
            new_rolls.append(roll)
    return new_rolls


def rerollDice(rolls):
    new_rolls = []
    for _ in rolls:
        new_rolls.append(random.randint(1, 6))
    return new_rolls


def multiplesStay():
    rolls = rollDice()
    original_rolls = rolls.copy()
    print(f"Original rolls: {original_rolls}")
   
    player_turn = 1
    while True:
        outcome_counts = countOutcomes(rolls)
        duplicates = {k: v for k, v in outcome_counts.items() if v > 1}      # copilot also helped me here
        
        if not duplicates:
            print("No duplicates left. Game over.")
            break
        
        if len(outcome_counts) == 1 and list(outcome_counts.values())[0] > 1:
            print(f"Player {player_turn} wins because there is only one duplicate left.")
            break
        
        user_input = input(f"Player {player_turn}, which number would you like to remove (must be a duplicate)? ")
        
        try:
            user_input = int(user_input)
            
            if outcome_counts.get(user_input, 0) > 1:
                rolls = removeOutcome(rolls, user_input)
                player_turn = 2 if player_turn == 1 else 1
                rolls = rerollDice(rolls)
                print(f"\nPlayer {player_turn} rerolled the dice. New rolls: {rolls}")
            else:
                print(f"{user_input} is not a duplicate. Try again.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        if not rolls:
            print("No more dice left. Game over.")
            break
multiplesStay()

