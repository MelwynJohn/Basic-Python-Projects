# importing Module Random
import random

#1st Part
# defining a function that asks user whether he/she wants to play again or not
def roll_dice():
    print("\nDo you want to Play again :) ? ")
    print("Enter Yes or No : ")
    choice = input()

#2nd Part
    #the question will be asked again if the user doesn't answer
    if choice == "":
        print("Wrong Input!! Enter Again Yes or No : ")
        choice = roll_dice()
    return choice

if __name__ == "__main__":
    print("Welcome to The Dice Game! ")
    dice_value = random.randint(1,6)
    print("YOU Got ", dice_value)
    choice = roll_dice()

    #3rd Part
    # The while loop below will continue until the user wants to end the game
    while choice:
        if choice == "No" or choice == "no":
            break
        elif choice == "Yes" or choice == "yes":
            dice_value = random.randint(1,6)
            print("YOU Got ", dice_value)
            choice = roll_dice()
        else:
            print("Wrong Input! Enter Again Yes or No : ")
            choice = roll_dice()

