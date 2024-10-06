# >1 Name and Next Birthday

ask_name = input("What is your name? ")
print(f"Hello, {ask_name}!")


user_age = int(input("How old are you? "))
user_age = user_age + 1
print(f"You will be {user_age} on your next birhtday!")



# >2 Fibonacci numbers into a list and the sum

fibonacci_list = [0,1] #Starting terms for the fibonacci sequence
while len(fibonacci_list) < 100: #First 100 fibonacci numbers
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2]) #equation for 'fib' list
print(f'\nFirst 100 Fibonacci numbers: {fibonacci_list}') #List of first 100 fibonacci nums
print(f'\nSum of the first 100 Fibonacci number sequence: {sum(fibonacci_list)}') #Sum of the first 100 fib nums



# >3 Read names into a list until user stops it then print the sorted list

names = []

while True:
    more_names = input("Give me a name to add to the list, press 0 to quit: ").strip().lower().capitalize()
    names.append(more_names)
    if more_names == '0':
        break

names.pop()
names.sort()

print('Your list of names:')
for name in names:
    print(name)

# print(names) # used for checking list 'names'    