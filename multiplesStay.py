import random

def rollDice():
    rolls = []
    for i in range(10):
        roll = random.randint(1,6)
        rolls.append(roll)
    return rolls
def countOutcomes(rolls):
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

def multiplesStay():
    rolls = rollDice()
    original_rolls = rolls.copy()
    print(f"Original rolls: {original_rolls}")
    while True:
        outcome_counts = countOutcomes(rolls)
        print(f"Outcome counts: {outcome_counts}")
        if len(outcome_counts) == 1:
            print("Only one unique number left. You lose.")
            break
        user_input = input(f"Which number would you like to remove (must be a duplicate)? ")
        try:
            user_input = int(user_input)
            if outcome_counts.get(user_input, 0) > 1:
                rolls = removeOutcome(rolls, user_input)
                print(f"Removed {user_input}. Remaining dice: {rolls}")
            else:
                print(f"{user_input} is not a duplicate. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        if not rolls:
            print("No more dice left. Game over.")
            break
multiplesStay()