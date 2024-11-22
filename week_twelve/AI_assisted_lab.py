# Problems:
# 1) Write a function that takes a string as input and returns
# a string where every character is doubled.

str_input = input("Type any word or sentence: ")
doubled_str = "".join(x*2 for x in str_input) #doubles the letter/spaces in a string
# unsure if spaces should be doubled
print(doubled_str)

# for word in str_input:
#     for letter in word: 
#         str_input2 = letter * 2
#         print(str_input2, end="") 
# # > Was printing before the account text? Also not optimal

# 2) Write a function that, when given a date, will tell you what 
# day (MTWTFSS) it is on.

from datetime import date
import calendar
my_date = date.today()
calendar.day_name[my_date.weekday()]

# 3) Write a function that takes in a matrix 'm' and a power 'p'
# and returns 'm' raised to the 'p'

# 4) write a function that generates random names

# 5) Write a monte carlo function that calculates the odds of
# drawing a royal flush