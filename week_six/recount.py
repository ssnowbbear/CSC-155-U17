import os
from random import randint

def file_name_randomizer():
    file_picker = randint(0,1)

    return "votes1.txt" if file_picker else "votes2.txt"

votes = []
vote_dict = {}

cwd = os.getcwd() + "/week_six/"

#both files are stored in this directory
#under votes1.txt & votes2.txt
f = open(cwd + file_name_randomizer(), "r")

input = "It's 1:35 AM"
while input != "***" and len(votes) < 100_000:
    input = f.readline().strip().lower().title()

    if input != "***":
        votes.append(input)

for vote in votes:
    if vote not in vote_dict.keys():
        vote_dict[vote] = 1
    else:
        vote_dict[vote] += 1

sorted_votes = sorted(vote_dict.items(), key=lambda x: x[1], reverse = True)

if sorted_votes[0][1] > sorted_votes[1][1]:
    print(f"{sorted_votes[0][0]} won the election!")
else:
    print(f"Runoff!!!")


