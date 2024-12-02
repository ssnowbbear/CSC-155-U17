# Problems:
# 1) Write a function that takes a string as input and returns
# a string where every character is doubled.

# str_input = input("Type any word or sentence: ")
# doubled_str = "".join(x*2 for x in str_input) #doubles the letter/spaces in a string
# unsure if spaces should be doubled
# print(doubled_str)

# for word in str_input:
#     for letter in word: 
#         str_input2 = letter * 2
#         print(str_input2, end="") 
# # > Was printing before the account text? Also not optimal

# 2) Write a function that, when given a date, will tell you what 
# day (MTWTFSS) it is on.

# from datetime import date
# import calendar

# my_date = date.today()

# str_weekday = calendar.day_name[my_date.weekday()] #Example ^
# #may need to be made inputtable? will work on later

# date_input = input("Enter a date in YYYY-MM-DD format: ")
# year, month, day = map(int, date_input.split('-')) #setting year, month, day
# date1 = date(year, month, day) #turning variables into a 'date'
# inp_weekday = calendar.day_name[date1.weekday()] #Finished

# print(inp_weekday)

# 3) Write a function that takes in a matrix 'm' and a power 'p'
# and returns 'm' raised to the 'p'

import numpy as np
from numpy.linalg import matrix_power

def matrixpower(m, p):
     """
     Take in a matrix and raise it to a power
     """
     return matrix_power(m, p)

# 4) write a function that generates random names

from random import choice

# def random_names():
#      """
#      generates random names
#      """
#      first_names = ("Carlos", "Jeremy", "Todd", "Darel", "Devon")
#      last_names = ("Flores", "Rodriguez", "Smith", "Williams", "Shaqira")
#      group = "".join(choice(first_names) + " " + choice(last_names))
#      return group

# print(random_names()) #checking if worked

# 5) Write a monte carlo function that calculates the odds of
# drawing a royal flush

from random import randint


# print(card_deck) # check card deck

def card_draw(card_deck):
     """
     drawing cards from a deck
     """
     current_hand = []
     for i in range(0,5):
        random_card = -1
        while random_card not in card_deck.keys():
            random_card = randint(0,51)
        # print(card_deck[random_card])
         
        current_hand.append(card_deck[random_card])
        del card_deck[random_card]  
     return current_hand

royal_flush = 0

for j in range(1_000_000):

    Suits = ['Club', 'Diamond', 'Heart', 'Spade']
    Ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    dict_keys = 0
    card_deck = {}

    for rank in Ranks:
        for suit in Suits:
            key, val = dict_keys, [rank, suit]
            card_deck.update({key : val})
            dict_keys += 1

    hand = card_draw(card_deck)
    rf_suit = hand[0][1]
    rf_possibilities = 0

    for card in hand:
        if Ranks.index(card[0]) > 7:
            if rf_suit == card[1]:
                rf_possibilities += 1



    if rf_possibilities == 5:
        royal_flush += 1
    
    print(royal_flush, j)

print(f"Odds of a royal flush: {(royal_flush/1_000_000)*100:.2f}%")
