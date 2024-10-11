# getting input for a kattis submission import sys

for line in sys.stdin:
    #each line is a string, same as using input()
    data = line
    print(data)

# kattis wont take user input like:
# data = input("Enter an input: ")
#print(data)

this_is_a_tuple = (3, 4, 5)
# print(this_is_a_tuple[0])

# this wont work, can't change value in a tuple
# this_is_a_tuple[0] = 45
# print(this_is_a_tuple.count(4))
# print(this_is_a_tuple.index(4))

# pointA = (4, 9) # is a tuple

