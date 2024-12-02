# 1)Write a function that takes a string as input and returns
# a string where every character is doubled.

import re

def remove_double_spaces(string):
    # Replace multiple spaces with a single space
    string = re.sub(r'\s+', ' ', string)
    return string

str_input = input("Type any word or sentence: ")
doubled_str = "".join(x*2 for x in str_input) #doubles the letter/spaces in a string
print(remove_double_spaces(doubled_str))

#2) Write a function that, when given a date, will tell you what
# day (MTWTFSS) it is on.

from datetime import date
import calendar

my_date = date.today()

str_weekday = calendar.day_name[my_date.weekday()] #Example ^
#may need to be made inputtable? will work on later

date_input = input("Enter a date in YYYY-MM-DD format: ")
year, month, day = map(int, date_input.split('-')) #setting year, month, day
date1 = date(year, month, day) #turning variables into a 'date'
inp_weekday = calendar.day_name[date1.weekday()] #Finished

print(inp_weekday)

#3) Write a function that takes in a matrix 'm' and a power 'p'
# and returns 'm' raised to the 'p'

def matrix_power(matrix, power):
    """
    Raise a matrix to a given power.

    Parameters:
    matrix (list of lists): The input matrix.
    power (int): The power to which the matrix should be raised.

    Returns:
    list of lists: The matrix raised to the given power.
    """
    if power == 0:
        return [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
    elif power == 1:
        return matrix
    else:
        half_power = matrix_power(matrix, power // 2)
        result = matrix_multiply(half_power, half_power)
        if power % 2 == 1:
            result = matrix_multiply(result, matrix)
        return result

def matrix_multiply(matrix1, matrix2):
    """
    Multiply two matrices.

    Parameters:
    matrix1 (list of lists): The first input matrix.
    matrix2 (list of lists): The second input matrix.

    Returns:
    list of lists: The product of the two matrices.
    """
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

#4) write a function that generates random names

import random

def generate_random_name():
    first_names = ["John", "Emily", "Michael", "Sarah", "William", "Olivia", "James", "Ava", "George", "Isabella"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"

# Example usage:
print(generate_random_name())  # Output: "Emily Wilson"

#5) Write a monte carlo function that calculates the odds of
# drawing a royal flushimport random

def monte_carlo_royal_flush(num_simulations):
    """
    Estimate the probability of drawing a royal flush using the Monte Carlo method.

    Parameters:
    num_simulations (int): The number of simulations to run.

    Returns:
    float: The estimated probability of drawing a royal flush.
    """
    royal_flush_count = 0

    for _ in range(num_simulations):
        deck = [i for i in range(52)]  # Create a deck of 52 cards
        random.shuffle(deck)  # Shuffle the deck
        hand = deck[:5]  # Draw 5 cards

        # Check if the hand is a royal flush
        royal_flush = (
            len(set([card // 13 for card in hand])) == 1  # All cards have the same suit
            and set([card % 13 for card in hand]) == {9, 10, 11, 12, 0}  # Cards are 10, J, Q, K, A
        )

        if royal_flush:
            royal_flush_count += 1

    return royal_flush_count / num_simulations

# Example usage:
num_simulations = 1000000
estimated_probability = monte_carlo_royal_flush(num_simulations)
print(f"Estimated probability of drawing a royal flush: {estimated_probability:.6f}")
