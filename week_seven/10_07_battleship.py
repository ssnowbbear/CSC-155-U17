#---------10-04 and 10-07-----------------

# twoDlist = [["00", "01", "02"],["10","11","12"], ["20","21","22"]]

# print(twoDlist)

# for item in twoDlist:
#     print(item)

# for i in range(len(twoDlist)):
#     for j in range(len(twoDlist[i])):
#         print(f"twoDlist[{i}][{j}]", twoDlist[i][j])




# build the game grid for each player
# "S" for ship, "H" for hit, "M" for miss, " " for blank 
from random import choice, randint


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
comp_missle_grid = {"a":["   ","   ","   ","   "], 
                  "b":["   ","   ","   ","   "], 
                  "c":["   ","   ","   ","   "], 
                  "d":["   ","   ","   ","   "]}
"""Computer's grid for missles fired"""
player_missle_grid = {"a":["   ","   ","   ","   "], 
                  "b":["   ","   ","   ","   "], 
                  "c":["   ","   ","   ","   "], 
                  "d":["   ","   ","   ","   "]}
"""Player's grid for missles fired"""
def print_grid(grid:dict):
    """
    Print the battleship game grid with nicely.
    """
    print("      1   2   3   4")
    print("    -----------------")
    for key in grid.keys():
        print(key, ": ", end="")
        for item in grid[key]:
            print(f"|{item}",end="")
        print("|")
        print("    -----------------")

print("Example Grid: ")
print_grid(player_ship_grid)
# Players place their ships
# Start with 1 ship, 2x1, on a 4x4
# Ask the user where there ship should be
# assume it is placed horizontally
ship_loc = input("Enter the coordinates to place the bow your ship (example a3):")
ship_row = ship_loc[0]
ship_col = (int)(ship_loc[1])-1
player_ship_grid[ship_row][ship_col] = " S "
player_ship_grid[ship_row][ship_col+1] = " S "


print_grid(player_ship_grid)

# place computer's ship
avail_rows = ['a','b','c','d']
comp_ship_row = choice(avail_rows)
comp_ship_col = randint(0,2)
comp_ship_grid[comp_ship_row][comp_ship_col] = " S "
comp_ship_grid[comp_ship_row][comp_ship_col + 1] = " S "


print_grid(comp_ship_grid)

# Players take turns calling out grid numbers

missle_loc = input("Enter the coordinates to launch your missile. (example a3):")
missle_row = missle_loc[0]
missle_col = (int)(ship_loc[1])-1

#if missile hits, update player missile grid and comp missile grid
if (comp_ship_grid[missle_row][missle_col] == " S "):
    comp_ship_grid[missle_row][missle_col] = " H "
else:
    player_missle_grid[missle_row][missle_col] = " M "


player_ship_grid[ship_row][ship_col] = " S "
player_ship_grid[ship_row][ship_col+1] = " S "

print("Player missile grid: ")
print(player_missle_grid)

# computer launches missile 
comp_missle_row = choice(avail_rows)
comp_missle_col = randint(0,2)

if(player_ship_grid[comp_missle_row][comp_missle_col]):
    player_ship_grid[comp_missle_row][comp_missle_col] = " S "

comp_ship_grid[comp_ship_row][comp_ship_col + 1] = " S "
#-----------------------------------------------------------
# Look online for ^above^ area, teacher started going faster



# Game continues until one player's ships have all been
# destroyed (no " S " left in ship grid)
# check player grid
player_loses = True
for row in player_ship_grid.keys(): 
    for col in range(len(player_ship_grid[row])):
        if (player_ship_grid[row][col] == " S "):
            player_loses = False
            break
    if (player_loses == False):
        break

comp_loses = True
for row in comp_ship_grid.keys():
    for col in range(len(comp_ship_grid[row])):
        if (comp_ship_grid[row][col] == " S "):
            comp_loses = False
            break
    if (comp_loses == False):
        break
print("Comp_loses:", comp_loses)
print("Player_loses:", player_loses)
#------Continue from here, remember to look online to find parts you missed (copy/paste new file)--------