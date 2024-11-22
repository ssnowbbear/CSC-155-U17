from random import randint

point = 0

wins = 0

def lose_win(sum_of_dice):
    """
    Defines when the player loses or wins
    """
    global point, wins
    if not point: 
        if sum_of_dice in [7, 11]: # win
            wins += 1
            return True
        elif sum_of_dice in [2, 3, 12]: # loss
            return True
    if point:
        if sum_of_dice == point: # win
            wins += 1
            return True
        if sum_of_dice == 7: # loss
            return True

def initial_values():
    """
    Sets all initial values back to their beginning state
    """
    global point
    point = 0

for i in range(1_000_000):
    while True:
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        sum_of_dice = dice1 + dice2

        game_end = lose_win(sum_of_dice) # determines if game_end is True or False

        if not point and sum_of_dice not in [2, 3, 7, 11, 12]: # allows the 'point' variable to be stored unchanged after initial roll
            point = sum_of_dice
                
        if game_end: # when the defined function is True
            initial_values()
            break

    print(i, wins) # keeping track

print(f"Odds of winnning: {(wins/1_000_000)*100:.2f}%")