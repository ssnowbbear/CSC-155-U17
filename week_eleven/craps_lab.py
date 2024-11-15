# > CRAPS Game <
# 1) Rules: 
# Each turn rolls two 6-sided dice
# On the first roll:
# - 7 or 11 wins.
# - 2, 3, or 12 loses.
# - Anything else will become the "point"
# If "point" was the outcome, rolling the "point" again wins.
# If "point" was the outcome, rolling a 7 loses.

# 2) After finishing the game, add in betting.
# (See if you can make it fun to play?)

# 3) After finishing bet system, find odds of winning.
# Use a Monte Carlo simulation, play 1 million (1_000_000) games
# Count the number of wins / (divided by) 1 million (1_000_000)
# Recommended to code this in a new file. There will likely be repeat code.

from random import randint

# > My dice <: 

dice1 = randint(1,6)
dice2 = randint(1,6)
sum_of_dice = dice1 + dice2

if sum_of_dice == 7:
    print("You Win!")
elif sum_of_dice == 11:
    print("You Win!")
elif sum_of_dice == 2:
    print("You Lose!")
elif sum_of_dice == 3:
    print("You Lose!")
elif sum_of_dice == 12:
    print("You Lose!")

#for after first roll
point = 0
first_roll_nums = [2, 3, 7, 11, 12]
if sum_of_dice not in first_roll_nums:
    point = sum_of_dice
    print(f"Point: {point}")
    
    
print(f"First dice: {dice1} \nSecond dice: {dice2} \nYou rolled: {sum_of_dice}")
