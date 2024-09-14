# >PROBLEM 1 (Max value in number list)

numbers = [7, 9, 10, 23, 2]
print(max(numbers))

# >PROBLEM 2 (Sum of numbers from 0-100)

sum = 0
for i in range(0,100):
    sum += i
print(sum)

# >PROBLEM 3 (Check if a list of numbers is sorted)

num_list = [5, 9, 23, 17, 59]
sorted_num = []

for num in num_list:
    sorted_num = []
    sorted_num.append(num)

sorted_num.sort()
# num_list.sort()

print(sorted_num)

if (num_list == sorted_num):
    print("These lists are the same")
else:
    print("You are dumb, do not do this")

# # if (sorted(num_list) == sorted_num):
# #     print(num_list)
# # else:
# #     print("You are dumb, do not do this")

# for idx in range():
#     sorted_num.append(idx)
# print(sorted_num)

# print([5, 9, 17, 23, 59])


# >PROBLEM 4 (Make a copy of an array(list),
# modify your copy and see if original is affected)

my_list = ['cars', 'chicken', 'potatoes', 'tacos', 'yo-yo']
my_list_copy = my_list

print(my_list)
print(my_list_copy)

my_list_copy.append('burritos')

print(my_list_copy)
print(my_list)

# >PROBLEM 5 (Program that will let me enter
# how many friends, enter friends' names,
# print out the friends in sorted order, one per line)

num_friends = (int)(input("How many friends? "))
friend = []

for i in range(num_friends):
    name_friends = (input('What is your friends name? '))
    friend.append(name_friends)

friend.sort()

for name in friend:
    print(name)

# print("\nnoodle", "\ncarrot")

# for name in(name_friends):
#     friends = []
#     friends.append(name)
#     friends.sort
#     print(friends)
# friends.append(name_friends)
# friends.sort()
# print(friends)