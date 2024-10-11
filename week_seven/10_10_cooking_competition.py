# > Cooking Competition 

# high scores good, low = bad
# need code that will work with any array of names and scores given

# names and scores given in parallel lists
names = ["Alan Ranch", "Anna Conda", "Bill Ding", "Brock Lee", 
         "Gail Force", "Hamilton Burger", "Rose Bush", "Tom Ato"]
scores = [4, 4, 0, 8, 8, 10, 8, 7]

# Alan Ranch = 4, Anna Conda = 4, Bill Ding = 0, Brock Lee = 8
# Gail Force = 8, Hamilton Burger = 10, Rose Bush = 8, Tom Ato = 7

# print(names[0], end= ' ')
# print(scores[0])

# Score of the winner 
winner = max(scores)

# Name of the winner
# Score of the person in last place
loser = min(scores)

# Name of the person in last place
# Average score
avg = (sum(scores)/len(scores))
print(f"The average of the contestants is: {avg}")

# Median score (middle number)

# Mode score (number that is repeated more than others)
for num in scores:
        
# Names of contestants whose score is equal to the mode 
# Names of contestants whose score is closest to average
# Names of contestants whose score is closest to median

# \/ When done with /\

# Print names of contestants in order of highest score to lowest score
# (print all names)
