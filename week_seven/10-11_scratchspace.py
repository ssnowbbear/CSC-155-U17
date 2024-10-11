player_ship_grid = {"a":["   ","   ","   ","   "], 
                    "b":["   ","   ","   ","   "], 
                    "c":["   ","   ","   ","   "], 
                    "d":["   ","   ","   ","   "]}

keys = list(player_ship_grid.keys()) #future proofing when grid becomes larger
print(keys)
keys = keys[0:-1] #a slice, when size of ships change, this will change
print(keys) #prints keys list minus the last index ("a", "b", "c")

row_idx =avail_rows.index(player_ship_row) #idx into list

[avail_rows[row_idx + 1]] # refers to index