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

