# > Cooking Competition 

# high scores good, low = bad
# need code that will work with any array of names and scores given

# names and scores given in parallel lists
names = ["Alan Rench", "Anna Conda", "Bill Ding", "Brock Lee", 
         "Gail Force", "Hamilton Burger", "Rose Bush", "Tom Ato"]

scores = [4, 4, 0, 8, 8, 10, 8, 7]

names_scores = dict(zip(names, scores)) # Dictionary of names and scores

# Score of the winner 
winner_score = max(names_scores.values())
print(f"The winner's score is: {winner_score}")

# Name of the winner
for name in names_scores.keys():
    if names_scores[name] == winner_score:
        print(f"The winner is: {name}")

# Score of the person in last place
loser_score = min(names_scores.values())
print(f"\nThe loser's score is: {loser_score}")

# Name of the person in last place
for name in names_scores.keys():
    if names_scores[name] == loser_score:
        print(f"The loser is: {name}")

# Average score
average = (sum(names_scores.values()))/(len(names_scores.values()))
print(f"\nThe average score is: {average}")

# Median score (middle number)
import statistics
sorted_names_scores = sorted(names_scores.values())
median_value = statistics.median(sorted_names_scores)
print(f"The median score is: {median_value}")

# Mode score (number that is repeated more than others)
# for num in scores:
mode_value = statistics.mode(names_scores.values())
print(f"The mode score is: {mode_value}")
        
# Names of contestants whose score is equal to the mode
print("\nThe contestant(s) who scored the same as the mode:")
for name in names_scores.keys():
    if names_scores[name] == mode_value:
        print(f"{name}")

# Names of contestants whose score is closest to average
closest_average = min(names_scores.values(), key=lambda x: abs(x - average))

print(f"\nThe contestant(s) with the score closest to the average is(are):")
for name in names_scores.keys():
    if names_scores[name] == closest_average:
        print(f"{name}")

# Names of contestants whose score is closest to median
closest_median = min(names_scores.values(), key=lambda x: abs(x - median_value))

print(f"\nThe contestant(s) with the score closest to the median is(are): ")
for name in names_scores.keys():
    if names_scores[name] == closest_median:
        print(f"{name}")

# \/ When done with /\

# Print names of contestants in order of highest score to lowest score
# (print all names)
reverse_sort = sorted(names_scores.items(), key=lambda x: x[1], reverse = True)

print(f"\nThe contestants from highest score to lowest score are as follows:")
for name, score in reverse_sort:
    print(f"{name}")