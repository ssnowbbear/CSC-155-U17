#---------------------------Guessing Game----------------------------
from random import randint

play_again = ""
guesses = [] 
while play_again != 'no':

    comp_choice = randint(1,100)

    user_guess = ""
    guess_count = 0
    while user_guess != comp_choice:

        user_guess = int(input("Enter a guess between 1-100: "))
        guess_count += 1

        lie = randint(1,10) == randint(1,10)

        if user_guess > comp_choice:
            if lie:
                print('Too low!')
            else:
                print('Too high!')

        elif user_guess < comp_choice:
            if lie:
                print('Too high!')
            else:
                print('Too low!')

    guesses.append(guess_count)
    print('You got it!')
    print(f'Number of Guesses: {guess_count}')
        
    play_again = input("Type 'No' to quit or anything else to continue: ").strip().lower()

loop_count = 0 # times through the for loop
for num in guesses:
    if len(guesses) == 1:
        print(f'Guesses per Game: {num}')
        break
    if loop_count == (len(guesses))-1:
        print(f'{num}')
        break
    if loop_count > 0 and loop_count < (len(guesses))-1:
        print(f'{num}, ', end='')
        loop_count += 1
        continue
    print(f'Guesses per Game: {num}, ', end='') # guesses per game
    loop_count += 1

print(f'Total Guesses: {sum(guesses)}') #total guesses
print(f'Total Games: {len(guesses)}') #games count
print(f'Average Number of Guesses: {int((sum(guesses))/(len(guesses)))}') #average of guesses

print("\nThank you for playing!")        
    
            
            

# make the computer lie 10% of the time x
# when the guess is correct, computer always says correct x
# keep track of number of guesses required by user x
# ask user if they want to play another game. x 
# number of games played x 
# number of guesses per game x
# average number of guesses x

