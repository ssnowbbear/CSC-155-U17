# >Indexing/Lists

fav_food_list = ["pizza", "brownie", "waffle", "cinnamon roll"]
# print(fav_food_list)
# print(fav_food_list[-1])
# print(fav_food_list[3])
# print(fav_food_list[(len(fav_food_list)-1)])
# >All ways to print the last item in a list

# >Build a list of double of int_list
int_list = [4, 12, 14, 5, 7]
doubles = []
for num in int_list:
    # doubles.append(num * 2)
    print(doubles)

# doubles2 = []
# for idx in range(len(int_list)):
    # print(doubles2)
    # print("idx=" ,idx)
    # print("int_list[idx] =" ,int_list[idx])
    # doubles2.append(int_list[idx]*2)

# >List Comprehension

# doubles3 = [x * 2 for x in int_list] # >List comprehension is MOST efficient. (Teachers hot take)
# print(doubles3) # (I do not know enought at thist time to say, but makes sense)


# doubles.extend(doubles2)
# print(doubles)
doubles.insert(2, 820)
print(doubles) # >Teacher is trying new things that she has not done in Python
