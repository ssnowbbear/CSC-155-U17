# > CRAPS Game <
# 1) Rules: >>> DONE <<<
# Each turn rolls two 6-sided dice
# On the first roll:
# - 7 or 11 wins.
# - 2, 3, or 12 loses.
# - Anything else will become the "point"
# If "point" was the outcome, rolling the "point" again wins.
# If "point" was the outcome, rolling a 7 loses.

# 2) After finishing the game, add in betting. >>> DONE <<<
# TODO: See if you can make it fun to play?

# TODO: 3) After finishing bet system, find odds of winning.
# Use a Monte Carlo simulation, play 1 million (1_000_000) games
# Count the number of wins / (divided by) 1 million (1_000_000)
# Recommended to code this in a new file. There will likely be repeat code.

from random import randint

# > Game <: 

keep_playing = ""
play_again = ""

point = 0

def lose_win(sum_of_dice):
    """
    Defines when the player loses or wins
    """
    global point, initial_money
    if not point: 
        if sum_of_dice in [7, 11]:
            print("\nYou Win!")
            initial_money = initial_money + bet_amount
            return True
        elif sum_of_dice in [2, 3, 12]:
            print("\nYou Lose!")
            initial_money = initial_money - bet_amount
            return True
    if point:
        if sum_of_dice == point:
            print("\nYou win!")
            initial_money = initial_money + bet_amount
            return True
        if sum_of_dice == 7:
            print("\nYou Lose!")
            initial_money = initial_money - bet_amount
            return True

def initial_values():
    """
    Sets all initial values back to their beginning state
    """
    global point
    point = 0


initial_money = float(input("Input the money you'd like to put in your betting pool: ")) # determines money pool

# print(bool(point)) # checking variables

while play_again != "no":
    bet_amount = float(input("Input amount you would like to bet from your betting pool: ")) # amount to bet from the initial_money

    while keep_playing != "no":
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        sum_of_dice = dice1 + dice2 
        
        # print(f"Point: {point}") # checked point variable before optimizing 
        
        game_end = lose_win(sum_of_dice) # determines if game_end is True or False

        if not point and sum_of_dice not in [2, 3, 7, 11, 12]: # allows the 'point' variable to be stored unchanged after initial roll
            point = sum_of_dice
        
        print(f"\nFirst dice: {dice1} \nSecond dice: {dice2} \nYou rolled: {sum_of_dice}") # info for the user
        
        if point:
            print(f"\nPoint: {point}") # the 'point' variable
        
        if game_end: # when the defined function is True
            initial_values()
            print(f"\nYour money pool is: {initial_money:.2f} \n\nGame Over!") #shows money pool
            break
        
        if initial_money == 0:
            break

        keep_playing = input("\nTo quit playing, type 'No.' To roll again type anything else: ").strip().lower()

    if initial_money == 0:
        print("\nOh no! We took all your money! You lose! ATM is around the corner!")
        break
    play_again = input("\nWould you like to play again? Type 'No' to quit, type anything else to play again: ").strip().lower()