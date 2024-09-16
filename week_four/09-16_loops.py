# start with an unsorted list of numbers

# list = [5,7,1,4,13,2,9,27,5,7]
# duplicate = []

# we want to find all duplicates
# approach 1: for each number, look through the list 
# to see if it has a duplicate, and create separate list
# if it does have a duplicate

# for idx in range(len(list)):
#     item = list[idx]
#     for idx2 in range(idx + 1, len(list)):
#         item2 = list[idx2]
        # print("item: ", item)
        # print("item2: ", item2)
        # if(item == item2):
        #     duplicate.append(item)
        #     print("Duplicate found!")
        #     break
# print(duplicate)
# print(list)

# approach 2: sort it first

# list.sort()
# duplicate2 = []

# for idx in range(len(list) - 1):
#     print("idx: ", idx)
#     if (list[idx] == list[idx+1]):
#         print("Duplicate Found!")
#         duplicate2.append(list[idx])
# print(duplicate2)

# Given a list of full names
# We want to see if anyone has the same last name

names = ['Brian May', 'Taylor Swift', 'Ozzy Osborne', 'Roger Taylor', 'Jamie Curtis', 'Richard Curtis']

#transform so last name comes first
last_names = []

for n in names:
    # split into first name and last name
    fn, ln = n.split()
    print(fn)
    print(ln)
    last_names.append(ln)

print(names)
print(last_names)

names.sort()
duplicate2 = []

for idx in range(len(names) - 1):
    print("idx: ", idx)
    if (names[idx] == names[idx+1]):
        print("Duplicate Found!")
        duplicate2.append(names[idx])
print(duplicate2)

# Messed something up ^^^, may need to look at code posted by instructor.