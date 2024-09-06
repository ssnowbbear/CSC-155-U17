#LAB Practice 2

names=["Sam","Kai","Adrian"]
#sam  is index 0! kai is index 1 etc.

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[-1])
# print(names[-2])
# print(names[-3])
#negatives come back from right side of the list. 
#'adrian' is first from right, so adrian = -1.
#'kai' = -2. 'sam' = -3

#>Length

# print(len(names))
#prints how man variables are in the list.

#>Numbers

scores = [3.3, 4.8, 2.2, 0.5]
#index acts the same as list of words

# print(sum(scores))
#adds the numbers in the list together

# print(max(scores)) 
#states the highest variable in the list
#min would do the opposite

#>Sort

# names.sort() #sort in place
# print(names)
#sorted lexicographically because upper and lower
#case letters and numbers need ordering
#before sort: sam=0, kai=1, adrian=2
#after sort: adrian=0, kai=1, sam=2

# print(sorted(names)) #sorting a copy

# names.reverse() # >will also reverse 
# print(names) #a previously sorted list
# reverse in place 

# print(list(reversed(names))) # >works, reverses the list
# print(reversed(names)) # >does not work, need to iterate
#what it is (list)

names.append("James")
# print(names) # >'.append' adds to
# an existing variable.

# >Removing

last = names.pop() # >'.pop' removes 'james'
# print(names) 
# print(last) # >prints 'james'

# >Modifying Elements ([])

# names[0] = "adrian"
# names.sort() #need parenthesis in order to sort the list
# print(names) # >'[0] causes 'adrian' to replace "Sam"

# >Finding an elements location

# print(names.index("Sam")) #if replaced by step ^, 
# python reads that 'sam' is not part of the list
# prints 'sam' index location which=0
# print(names.index("Kai")) # index 1
# print(names.index("Adrian")) # index 2

# >Looping Through Arrays

# for name in names:
    # print(name) #prints in a 'loop' (down)

# >Iteration Ex. "name" and how long "name" is

# for name in names: #need the colon
    # print(name,len(name)) # >len=length and asks
# python to print the length of the name

# >Range

# for i in range(5): # >prints 0, 1, 2, 3, 4 in loop
    # print(i) # >i=int=integer

# for num in range(2,7):
    # print(num) # >prints 2-6 in loop but not 7

# >Index while looping

# for i in range(len(names)): # >could also use enumerate
    # print(names[i]) # >prints the list in loop
# >'i' starts at index '0'

# for i in range(len(names)):
    # print(i,names[i]) # >first i grabs the index
# number and prints it in front of the names
# in loop form

# >List of Squares

# squares = [] #squares starts as an empty list
# for val in range(1,11):
    # squares.append(val**2)
# print(squares) # >prints the square roots from 1-10
# does not print the square root of 11.
# range will be one value higher than printed format

# squares = [val**2 for val in range(1,11)] 
# print(squares) #> different way to print same
# previous list

# >Tuple
# a tuple cannot be changed whereas a list can be

# tup = ('Sam', 'Kai', 'Adrian')
# print(tup)

# ----- WORKOUT PROBLEMS THEN MOVE TO NEW FILE------

# >PROBLEM 1 (Max value in number list)

# numbers = [7, 9, 10, 23, 2]
# print(max(numbers))

# >PROBLEM 2 (Sum of numbers from 0-100)

for i in range(0,101):
    print(i+i)

# >PROBLEM 3 (Check if a list of numbers is sorted)


# >PROBLEM 4 (Make a copy of an array,
# modify your copy and see if original is affected)

# >PROBLEM 5 (Program that will let me enter
# how many friends, enter friends' names,
# print out the friends in sorted order, one per line)