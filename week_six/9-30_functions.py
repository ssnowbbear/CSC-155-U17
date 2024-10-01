# -----------LOOK ONLINE FOR FIRST HALF---------------
# Functions 

# 'return' can pull a variable out of a function it was created in(for loop was the example)
# referred to as the 'scope'
# only the value gets returned

def sum21lists(a,b):
    total = sum(a)
    total = total + sum(b)




# Print a list nicely

# def nice_print(string_list):
#     for item in string_list:
#         print(item)

# # print(list1)


# string_list = ['Hi, ','how are you']

# print(string_list) # prints '['Hi, ', 'how are you']
# nice_print(string_list) # prints 'Hi, (new line) how are you'
# nice_print will not work outside of scope

# another function

# from random import choice

def coin_flip():
    from random import choice #apparently can be used inside function
    coin = ["heads", "tails"]
    return choice(coin)

heads = 0
tails = 0

for i in range(100):
    flip = coin_flip()
    if (flip == "heads"):
        heads += 1
    else:
        tails += 1
print("Heads: ", heads)
print("Tails: ", tails)

# Another way to do the same thing ^
heads = 0
tails = 0
from random import randint
for i in range(100):
    flip = randint(1,2)
    if flip == 1:
        heads += 1
    else:
        tails += 1
print("Heads: ", heads)
print("Tails: ", tails)