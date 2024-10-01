# >Problem 1

user_name = input("What is your name? ")
user_name = user_name.strip().title()

if(user_name == "Bob"):
    print("Good morning Bob")
if(user_name == "Alice"):
    print("Hello, Alice")
else:
    print("Go away.")

    # >2 (2,000,000 coin flips and count)

import random

num_flip = 2000000

heads = 0
tails = 0

for i in range(num_flip):
    if random.randint(0,1) == 0:
        heads += 1
    else:
        tails += 1

print(f'Heads: {heads}')
print(f'Tails: {tails}')

# >3 (Dice roll 2,000,000 times)

import random

num_rolls = 2000000

num_of_5 = 0

for i in range(num_rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 == 5  or dice2 == 5:
        num_of_5 += 1
    if dice1 + dice2 == 5:
        num_of_5 += 1

print(f'Times 5 rolled: {num_of_5}')

for num in range(num_of_5):
    odds = num / num_rolls
percent = float(odds) * 100

print('Odds of a 5: ', odds)
print('Percent of time 5 was rolled:', percent,'%')