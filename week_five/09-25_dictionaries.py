# > Dictionaries

# my_dictionary = {0: 'rock', 1: 'paper', 2: 'scissors'} # Can switch the integer and string
# # Can map anything to anything in a dictionary

# print(my_dictionary[0])

# my_dictionary[3] = 'potato' #adds to my_dictionary

# for key in my_dictionary.keys():
#     print(my_dictionary[key])

# for value in my_dictionary.values():
#     print(value)

# for key, value in my_dictionary.items():
#     print('The key is: ', key)
#     print('The value is: ', value)

# my_dictionary.pop(2) # removes item by index location

# for key, value in my_dictionary.items():
#     print('The key is: ', key)
#     print('The value is: ', value)

# new_keys = [1,3,5,7,9]
# new_values = ['pineappes', 'bananas', 'truck', 'car', 'tricycle']

# for i in range(len(new_keys)):
#     nk = new_keys[i]
#     # if the key is not in the dictionary, add the key
#     if (not(nk in my_dictionary.keys())):
#         #look online for how to finish, didn't get in time!

ages = {'Alice':19, 'Bob':23, 'Charlie':19}

for key, value in ages.items():
    print('Their name is: ', key)
    print('Their age is: ', value)