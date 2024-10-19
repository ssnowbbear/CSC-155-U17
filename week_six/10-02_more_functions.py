
# list1 = [1, 23, 4, 5, 8]
# list2 = [5, 7, 11, 15, 27]

# # sum2lists with type hinting
# def sum2lists(a:list, b:list)->int:
#     """
#     Returns the integer sum of two lists, a and b, that contain integers.
#     """
#     # Docstrings ^, function documentation?, teacher googled in class
#     total = sum(a) + sum(b)

# list2.sort()
# sum()

# print(sum2lists(list1, list2))


# Roll dice function
# Lab 3, teachers edition

from random import randint
# '= 6' is a 'default value'. so default is 6 sided die
def dice_roll(sides = 6)->int:
    """
    Simulate a single dice roll using a "siides" -sided die.
    Returns the roll result.
    """
    return randint(1, sides)

# simulate 2_000_000 rolls of 2 six-sided dice, summed
# track the number of times we roll 7

# sevens = 0
# for i in range(2000000):
#     total = dice_roll() + dice_roll()
#     if total == 7:
#         sevens += 1
#     # print(total)
# print(sevens, "7's were rolled.")
# pct = sevens / 2000000 * 100
# print("Percent of sevens rolled: ", pct)

# Write a function for a damage roll

def dmg_roll(num_dice:int, num_sides = 4)->int:
    """
    Rolls num_dice dice, which each num_sides sides.
    Returns the sum of all rolled dice.
    """
    total = 0
    for i in range(num_dice):
        total += dice_roll(num_sides)

    print("hello")
    return total

(dmg_roll(4))