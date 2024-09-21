# > LAB 3
#   >Problem 1 (Ask user for name. If 'user'
#   >name = bob or alice, great them. If not,
#   >tell them to go away)

# user_name = input("What is your name? ")

# if(user_name == "Bob"):
#     print("Good morning Bob")
# elif(user_name == "Alice"):
#     print("Hello, Alice")
# else:
#     print("Go away.")


# Power Point notes!!!!!-----------------------

# from random import randint 

#random is a python module containing pseudo-random number generators
#randint is a python function that returns random number between two numbers
#each number is equally likely to happen

# dice = randint(1,6)
# dice2 = randint(1,6)
# print("Dice 1: ", dice, "\nDice 2: ", dice2)

# How can we roll two dice? (already did, transformed from one dice ^)
# there is a right and wrong way to do this (my way seems to have worked)



# > Conditional Tests 

#these evaluate to a Boolean value: True or False

# name = 'Alice'
# print(name == 'Bob') #prints false

# print(3<=5) #prints true

# > If

# if 3 < 5:
    # print('I happened') #prints I happened
# else:
    # print('No, I did')  #does not print

# EX 2:

# if 3 == 5:
    # print('I happened') #does not print
# else:
    # print('No, I did') #prints No, I did 

# >If statements in general

# 'if' condition:
    #this code runs if 'condition' is True
# 'else':
    #this code runs if 'condition' is False
#runs after the if-else
#do not always need the 'else'

# > Flip a coin

#program to flip a coin that prints heads out 50% and tails other 50%

# from random import randint

# coin = randint(1,2)

# if coin == 1:
    # print('Heads')
# else:
    # print('Tails')

# >Grades

#test for multiple conditions before the else

# grade = int(input('Enter grade (0-100): '))

# if grade > 90:
    # print ('A')
# elif grade > 80:
    # print('B')
# elif grade > 70:
    # print('C')
# elif grade > 60:
    # print('D')
# else:
    # print('F')

#Asks for percent of grade then gives associated letter

x = 3

#multiple conditions 

# print(x < 4 and x > 2)
# print(x < 4 and x != 3)
# print(x < 4 or x != 3)
# print(x < 3 or x !=3)

# if 2 <= x <5:
    # print('comparisons can be chained')

# > Ranges

#flip 10 coins

from random import randint

# for i in range(10): # *2 will print 20
    # if randint(1,2)==1:
        # print('heads')
    # else:
        # print('tails')

# > Multiple Functions from the Same Module

#separate by comma

from random import randint, choice

# or import module and use '.' to indicate which you want 

import random

# print(random.randint(1,2))
# print(random.choice([1,2]))

# ----------------Problems 2 & 3----------------------

# >2 (2,000,000 coin flips and count)

import random

num_flip = 2000000

heads = 0
tails = 0

for i in range(num_flip):
    if random.randint(0,1) == 0:
        heads += 1
    else:
        tails += 1

print(f'Heads: {heads}')
print(f'Tails: {tails}')

# >3 (Dice roll 2,000,000 times)

import random

num_rolls = 2000000

num_of_5 = 0

for i in range(num_rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 == 5  or dice2 == 5:
        num_of_5 += 1

print(f'Times 5 rolled: {num_of_5}')

for num in range(num_of_5):
    odds = num / num_rolls
percent = float(odds) * 100

print('Odds of a 5: ', odds)
print('Percent of time 5 was rolled:', percent,'%')