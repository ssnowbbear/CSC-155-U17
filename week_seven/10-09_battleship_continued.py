# Battleship game, day 2


from random import choice, randint

# build the game grid for each player
# "S" for ship, "H" for hit, "M" for miss, " " for blank 





comp_ship_grid = {"a":["   ","   ","   ","   "], 
                  "b":["   ","   ","   ","   "], 
                  "c":["   ","   ","   ","   "], 
                  "d":["   ","   ","   ","   "]}
"""Computer's ship grid: a dictionary of lists, 4x4"""
player_ship_grid = {"a":["   ","   ","   ","   "], 
                    "b":["   ","   ","   ","   "], 
                    "c":["   ","   ","   ","   "], 
                    "d":["   ","   ","   ","   "]}
"""Player's ship grid: a dictionary of lists, 4x4"""
comp_missile_grid = {"a":["   ","   ","   ","   "], 
                  "b":["   ","   ","   ","   "], 
                  "c":["   ","   ","   ","   "], 
                  "d":["   ","   ","   ","   "]}
"""Computer's grid for missiles fired"""
player_missile_grid = {"a":["   ","   ","   ","   "], 
                  "b":["   ","   ","   ","   "], 
                  "c":["   ","   ","   ","   "], 
                  "d":["   ","   ","   ","   "]}
"""Player's grid for missiles fired"""
def print_grid(grid:dict):
    """
    Print the battleship game grid nicely.
    """
    print("      1   2   3   4")
    print("    -----------------")
    for key in grid.keys():
        print(key, ": ", end="")
        for item in grid[key]:
            print(f"|{item}",end="")
        print("|")
        print("    -----------------")
print("Example grid:")
print_grid(player_ship_grid)
# Players place their ships
# Start with 1 ship, 2x1, on a 4x4
# Ask the user where there ship should be
# assume it is placed horizontally

avail_rows = ['a','b','c','d']
valid_row = False
valid_column = False
while (valid_row == False or valid_column == False):
    ship_loc = input("Enter the coordinates to place the bow your ship (example a3):")
    player_ship_row = ship_loc[0]
    if (player_ship_row in avail_rows):
        valid_row = True
    else:
        print("Invalid row")
        valid_row = False 
    try:
        player_ship_col = (int)(ship_loc[1])-1
    except:
        print("Please enter a number for the column.")
    
    if (player_ship_col >= 0 and player_ship_col < len(player_missile_grid["a"])):
        valid_column = True
    else:
        print("Invalid column.")
        valid_column = False

    player_ship_grid[player_ship_row][player_ship_col] = " S "
    player_ship_grid[player_ship_row][player_ship_col+1] = " S "

print("Player's missile Grid")
print_grid(player_missile_grid)
print("Player's Ship Grid")
print_grid(player_ship_grid)

# place computer's ship

comp_ship_row = choice(avail_rows)
comp_ship_col = randint(0,2)
comp_ship_grid[comp_ship_row][comp_ship_col] = " S "
comp_ship_grid[comp_ship_row][comp_ship_col+1] = " S "


# # TODO: take this out later!
# print("Computer Ship Grid")
# print_grid(comp_ship_grid)

player_loses = False
comp_loses = False
while(player_loses == False and comp_loses == False):
    # Players take turns calling out grid numbers
    # If the opposite player calls a grid location that
    # overlaps one of your ships, it's a hit, otherwise it's
    # a miss

# grabbed while loop from above to use for missile location, copy into new file once posted online
# ctrl + f will find and replace a word
    missile_loc = input("Enter the coordinates to launch a missile (example a3):")
    missile_row = missile_loc[0]
    missile_col = (int)(missile_loc[1])-1

    # if missile hits, update player missile grid and computer's ship grid
    if (comp_ship_grid[missile_row][missile_col]== " S "):
        comp_ship_grid[missile_row][missile_col] = " H "
        player_missile_grid[missile_row][missile_col] = " H "
    else:
        player_missile_grid[missile_row][missile_col] = " M "

    # # TODO: take this out later!
    # print("Computer Ship Grid")
    # print_grid(comp_ship_grid)

    print("Player missile Grid")
    print_grid(player_missile_grid)
    print("Player Ship Grid")
    print_grid(player_ship_grid)
    

    valid_launch = False
    while(valid_launch == False):
        # computer launches missile
        comp_missile_row = choice(avail_rows)
        comp_missile_col = randint(0,3)
        if(comp_missile_grid[comp_missile_row][comp_missile_col] == "   "):
            valid_launch = True

    print("Computer launched missile at", f"{comp_missile_row}{comp_missile_col + 1}")
    if (player_ship_grid[comp_missile_row][comp_missile_col] == " S "):
        player_ship_grid[comp_missile_row][comp_missile_col] = " H "
        comp_missile_grid[comp_missile_row][comp_missile_col] = " H "
    else:
        comp_missile_grid[comp_missile_row][comp_missile_col] = " M "
        player_ship_grid[comp_missile_row][comp_missile_col] = " M "

    print("Player missile Grid")
    print_grid(player_missile_grid)
    print("Player Ship Grid")
    print_grid(player_ship_grid)

    # TODO: remove later
    # print("Computer Ship Grid")
    # print_grid(comp_ship_grid)



    # Game continues until one player's ships have all been
    # destroyed (no " S " left in ship grid)
    #check player grid
    player_loses = True
    for row in player_ship_grid.keys():
        for col in range(len(player_ship_grid[row])):
            if (player_ship_grid[row][col] == " S "):
                player_loses = False
                break
        if(player_loses == False):
            break
    comp_loses = True
    for row in comp_ship_grid.keys():
        for col in range(len(comp_ship_grid[row])):
            if (comp_ship_grid[row][col] == " S "):
                comp_loses = False
                break
        if (comp_loses == False):
            break

    # print("Comp_loses:", comp_loses)
    # print("Player_loses:", player_loses)

if player_loses:
    print("So sad, you lost!")
else:
    print("Yay, you won!")

    # Copy full file into a new file so you have the whole program to look back on!!!!!