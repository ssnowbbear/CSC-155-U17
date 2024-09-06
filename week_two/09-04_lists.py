
# my_variable = "5"
# print(type(my_variable))

fav_food = "chocolate"
fav_food2 = "ice cream"
fav_food3 = "bananas"
fav_food4 = "strawberries"

# print(fav_food)
# print(fav_food2)
# print(fav_food3)
# print(fav_food4)

fav_food_list = [fav_food, fav_food2, fav_food3, fav_food4]

# print(fav_food_list)

int_list = [1, 2, 3, 4, 5]

# print(int_list)

mixed_list = [fav_food, 4, 5, 6.7]

# print(mixed_list)

mixed_list2 = [fav_food_list, int_list]

# print(mixed_list2)

#>Last index available is 1 less than your total list.

# print(fav_food_list[1])

#>Brackets next to your list accesses that number index.

# print(fav_food_list[-1])

fav_food_list.append("cake")

# print(fav_food_list)
# print(len(fav_food_list))

fav_food_list.remove("bananas")

# print(fav_food_list)
# print(len(fav_food_list))

#>'Append' adds to your list, 'remove' (clearly) removes from the list.
#>'Remove' takes out the first item in cases of same variables.
#>'Len" will count the variables in the list.

# print(sum(int_list))

#>Use a 'for' loop to print all 'fav_food'

# for food in fav_food_list:
    # print(food)

# for f in fav_food_list:
    # print(f)
    # print(f.upper())

#>Need colon and tabbed in for 'for' loop

print(sum(int_list))
total = 0

for i in int_list:
    total += i
    print("Total: ", total)

