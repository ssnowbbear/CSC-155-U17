# >Random/Randint

from random import randint
from random import choice

#Important to import item before you attempt to use it in your code

# for i in range(100):
    # dice_roll = randint (1,6)
    # print(dice_roll) 

# REMEMBER FOR LAB 3!!!!!!!
# num_sides = (int)(input("Enter a number of sides: "))
# num_rolls = (int)(input("Enter the number of rolls: "))
# for i in range(num_rolls):
    # dice_roll = randint (1, num_sides)
    # print("You rolled", dice_roll) 


# Same as above
# import random 

# dice_roll = random.randint(1,6)

# Some tools for rock paper scissors challenge!!!!!!
# cars = ['corvette', 'mustang', 'camaro', 'viper', 'charger', 'challenger']
# print(choice(cars))
# chosen_car = choice(cars)
# if (chosen_car == 'corvette'):
#     print("Corvettes look like ferraris now")
# elif (chosen_car == "viper"):
#     print("Vipers are known as a death trap")
# elif (chosen_car == "mustang"):
#     print("Fords are stupid")
# elif (chosen_car == "camaro"):
#     print("You own a camaro")
# else:
#     print("I dont feel like continuing to type")

# > PIN Generator
num_digits = (int)(input("Enter the number of digits:"))

# All digits at once
print("Your random PIN is: ", randint(0,10**num_digits))


# > Password Generator
#   generate a random number 0-255
#   convert ascii using chr = character
#   repeat length times
#   Google ascii ('as-key') table
#   CHECK PHONE FOR CODE


#ROCK PAPER SCISSORS CHALLENGE
rock_paper_scissors = ['rock', 'paper', 'scissors']