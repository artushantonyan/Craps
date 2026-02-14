import random

# Gives a random number between 1 and 6.
def roll_die():
    return random.randint(1, 6)


# We roll two dice and return their sum.
def roll_dice():
    die1 = roll_die()
    die2 = roll_die()
    total = die1 + die2
    return total
    print(f"You rolled a {die1} and a {die2}")
    print(f"Total is: {total}")
    return total                


# First roll condition
def play_game():               
    print("Welcome to Craps!")

    first_roll = roll_dice()

    if first_roll == 7 or first_roll == 11:
        print("You win!")

    elif first_roll == 2 or first_roll == 3 or first_roll == 12:
        print("Casino wins!")

    else:
        goal = first_roll
        print("Your goal number is:", goal)
        print("Keep rolling...")

        while True:
            new_roll = roll_dice()
            print("You rolled:", new_roll)
            if new_roll == goal:
                print("You win!")
                break
            elif new_roll == 7:
                print("Casino wins!")
                break
play_game()