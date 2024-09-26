#------------STOPPED @ 34 MINUTES!------------------------------------------

# make a game where we echo back to user in alternate case
# (ExAmPlE tExT), keep going until user inputs 'no'

# DO NOT SET true = False!
# repeat until user inputs 'no', 'n'
# use a boolean variable as sentinel

# keep_playing = True # <- Boolean variable, can only be true or false
# while(keep_playing):
#     # get user input
#     user_phrase = input("Enter a phrase to echo: ")
#     # convert user input to alternate case

#     # to end our loop, user must type 'n'
#     play_again = input("Enter 'n' to quit, or press any key to continue: ")
#     if (play_again == 'n'):
#         keep_playing = False


# Example of infinite loop
# while(True):
    # print("This is the song that never ends")




# FOR COFFEE LAB

order_again = input("Will that be all for you today? ")
order_again = order_again.lower().strip()

if (order_again == "yes"):
    print("Have a good day! Please come again")
else:
    print("What else can I help you with?")

# Will need to be part of a loop? While loop or for loop?
# Is not operating properly. Is operating by case sensitivity
# Figure out how to respond to 'else' statement