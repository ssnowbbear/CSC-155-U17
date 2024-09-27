# Guessing Game
from random import randint
from random import choice

# number of games played
# number of guesses per game
# average number of guesses

while True:
    comp_choice = randint(1,100)
    while True:
        user_guess = int(input("Enter a guess between 1-100: "))
        if user_guess > comp_choice:
            print('Too high!')
        elif user_guess < comp_choice:
            print('Too low!')
        elif user_guess == comp_choice:
            print('You got it!')
            break
            
    play_again = input("Press 'n' to quit or any other key to continue: ")
    play_again = play_again.strip().lower()
    if (play_again == 'n'):
        print("Thank you for playing!")
        break
            
            

# make the computer lie 10% of the time
# when the guess is correct, computer always says correct

# keep track of number of guesses required by user

# ask user if they want to play another game. 