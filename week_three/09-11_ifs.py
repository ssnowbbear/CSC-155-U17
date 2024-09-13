# >IF's

# user_response = input("What is your favorite treat?")

# if (user_response == "chocolate"):
#     print("Cool, I like chocolate, too!")
# else:
#     print("That's cool, but I think chocolate is better")

# print("Thanks for playing!")

# User's favorite color

# user_color = input("What is your favorite color? ")
# user_color = user_color.lower().strip() # > .lower() allows for upper and lowercase letters in response. > .strip allows spaces in response
# # .upper() is the opposite of .lower() if given response is in uppercase

# # if (user_color == "red"):
# #     print("Roses are red")
# # elif (user_color == "yellow"):
# #     print("Bananas are yellow")
# # elif (user_color == "blue"):
# #     print("The sky is blue")
# # else:
# #     print("That's a pretty color")

# match user_color: # >Different way to do 'if' 'else' statements
#     case "red":
#         print("Roses are red!")
#     case "yellow":
#         print("Bananas are yellow!")
#     case "blue":
#         print("The sky is blue!")
#     case _:
#         print("Wow, that's neat")

# num1 = (int)(input("Please enter a number: "))
# num2 = (int)(input("Please enter another number: "))

# > Example of a logic error
# if (num1 >= num2): # Can use <, > instead of >= in order to allow system to recognize when numbers are equal
#     print("The second number was smaller.")
# else:
#     print("The second number was equal or greater.")

# if (num1 > num2 or num1 == num2): # > or statement cancels out elif num1 == num2 statement
#     print("The first number is greater than or equal to the second")
# # elif (num1 == num2):
#     # print("The first number is the same as the second number")
# else:
#     print("The second number is greater than the second")

# More user color:

user_color = input("What is your favorite color? ")
user_color = user_color.lower().strip()

#if its red or yellow, it's a warm color, otherwise it's a cool color
if (user_color == "red" or user_color == "yellow"):
    print(f"{user_color.capitalize()} is a warm color")
elif (user_color == "green" or user_color == "blue"):
    print(f"{user_color.capitalize()} is a cool color")
else: # >Look at online code file to finish out notes