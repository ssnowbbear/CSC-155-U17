# Dictionary Lab
# >Notes

# empty dictionary

# d = {}

# # dictionaries allow for key, value pairing

# d[3] = 'cat'
# d['text'] = 123

# print(d)

# ex 2

# age = {}

# age['Zach'] = 33

# # Birthday

# age['Zach'] += 1 

# print(age['Zach'])

# ex 3 {key : value, key2 : value2, etc}

# ages = {'Noah' : 24, 'Zach' : 33, 'Alice' : 22}

# # common ways to iterate through a dictionary
# for name in ages.keys():
#     print(name)

# for age in ages.values():
#     print(age)

# for name, age in ages.items():
#     print(name,age)

# frequency an element appears in a sentence

# repeat_words = {}

# sentence = input("Enter a sentence and I will count how many times each word is used: ")

# for word in sentence.split():
#     if word not in repeat_words:
#         repeat_words[word] = 1
#     else:
#         repeat_words[word] += 1

# print(repeat_words)

# 1) Program that reads in numbers until the user enters 0.
# Use a dictionary to count how often each number appears

keep_adding = ""
numbers = {}

while keep_adding != "0":
    
    for num in keep_adding.split():
        if num not in numbers:
            numbers[num] = 1
        else:
            numbers[num] += 1

    keep_adding = input("Type a number and I will keep track of how many times it has appeared, enter 0 to end: ")
print(numbers)