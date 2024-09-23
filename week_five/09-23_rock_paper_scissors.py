# >Build a rock paper scissors game
#   get the user response

# resp = ""
# while (resp != 'r' and resp != 'p' and resp !='s'):
#     resp = input('Enter r for rock, p for paper, s for scissors: ')
# #clean and transform
# resp = resp.strip().lower()

# # kill the game if they didnt enter r, p, or s
# # if (resp == 'r' or resp == 'p' or resp == 's'):

# #   generate the computer response

# possible_responses = ['r', 'p', 's']
# from random import choice
# comp = choice(possible_responses)

#   report who won or kill the game

# if (resp == 'r'):
#     if(comp == 's'):
#         print('You win!')
#         print('Computer chose scissors.')
#     elif(comp == 'p'):
#         print('Computer chose paper.')
#         print('You lose.')
#     else:
#         print('Computer chose rock.')
#         print('You tied')

# if (resp == 's'):
#     if(comp == 'p'):
#         print('You win!')
#         print('Computer chose paper.')
#     elif(comp == 'r'):
#         print('Computer chose rock.')
#         print('You lose.')
#     else:
#         print('Computer chose scissors.')
#         print('You tied')

# if (resp == 'p'):
#     if(comp == 'r'):
#         print('You win!')
#         print('Computer chose rock.')
#     elif(comp == 's'):
#         print('Computer chose scissors.')
#         print('You lose.')
#     else:
#         print('Computer chose paper.')
#         print('You tied')

# else:
#     print('Sorry, I do not understand your choice')

#same as above but with gracefull input handle

# if (resp == 'r'):
#     if(comp == 's'):
#         print('You win!')
#         print('Computer chose scissors.')
#     elif(comp == 'p'):
#         print('Computer chose paper.')
#         print('You lose.')
#     else:
#         print('Computer chose rock.')
#         print('You tied')

# if (resp == 's'):
#     if(comp == 'p'):
#         print('You win!')
#         print('Computer chose paper.')
#     elif(comp == 'r'):
#         print('Computer chose rock.')
#         print('You lose.')
#     else:
#         print('Computer chose scissors.')
#         print('You tied')

# if (resp == 'p'):
#     if(comp == 'r'):
#         print('You win!')
#         print('Computer chose rock.')
#     elif(comp == 's'):
#         print('Computer chose scissors.')
#         print('You lose.')
#     else:
#         print('Computer chose paper.')
#         print('You tied')

# else:
    # print('Sorry, I do not understand your choice')

keep_playing = 'y'

while(keep_playing != 'n'):
    resp = ""
    while (resp != 'r' and resp != 'p' and resp !='s'):
        resp = input('Enter r for rock, p for paper, s for scissors: ')
#clean and transform
    resp = resp.strip().lower()

# kill the game if they didnt enter r, p, or s
# if (resp == 'r' or resp == 'p' or resp == 's'):

#   generate the computer response

    possible_responses = ['r', 'p', 's']
    from random import choice
    comp = choice(possible_responses)

    if (resp == 'r'):
        if(comp == 's'):
            print('You win!')
            print('Computer chose scissors.')
        elif(comp == 'p'):
            print('Computer chose paper.')
            print('You lose.')
        else:
            print('Computer chose rock.')
            print('You tied')

    if (resp == 's'):
        if(comp == 'p'):
            print('You win!')
            print('Computer chose paper.')
        elif(comp == 'r'):
            print('Computer chose rock.')
            print('You lose.')
        else:
            print('Computer chose scissors.')
            print('You tied')

    if (resp == 'p'):
        if(comp == 'r'):
            print('You win!')
            print('Computer chose rock.')
        elif(comp == 's'):
            print('Computer chose scissors.')
            print('You lose.')
        else:
            print('Computer chose paper.')
            print('You tied')

#ask user if they want to keep playing

        keep_playing = input('Enter n to quit, or any other key to continue')
        keep_playing = keep_playing.strip().lower()
        print(keep_playing)
        #could not get this ^ to print. look at class code online