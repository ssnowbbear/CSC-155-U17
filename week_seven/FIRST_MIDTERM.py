# > 1 Program that counts vowels in a user inputted line.

# user_line = str(input("Enter a line: ")).lower() #takes an input from the user and lower cases it

# vowels = ["a", "e", "i", "o", "u"] #list of vowels

# vowel_count = 0 #keeps track of vowels in 

# for letter in range(len(user_line)): #loops through sentence
#     if user_line[letter] in vowels: #looks if letter in user_line is in list of vowels
#         vowel_count += 1 #increases vowel count

# print(f"Vowels used in your sentence: {vowel_count}")
#----------------------------------------------------------------------

# > 2 How many people and their ages sorted oldest to youngest. 
    # Print the most common age

# people = {}

# people_count = (int(input("How many people? ").strip()))

# for int in (range(people_count)):
#     name_of_people = input("Enter person and age: ").strip().capitalize().split()
#     key, val = name_of_people
#     people.update({key:val})

# sort_people = sorted(people.items(), key=lambda x: x[1], reverse=True)

# print("\nOldest to youngest:")
# for name, age in sort_people:
#     print(f"{name}")

# ages_list = list(people.values())
# common_age = max(set(ages_list), key = ages_list.count)
# print(f"\nMost common age: {common_age}")

# import operator
# sorted_name_age = sorted(name_age.items(), key=operator.itemgetter(1))
# ^ did not work how i wanted it to, other way seemed more simple
#-------------------------------------------------------------------

# > 3 Function that is passed in a list of points (tuples) and returns the average distance between the points

# def dmg_roll(num_dice:int, num_sides = 4)->int:

test1 = [(0,0), (0,1), (0,2)]

xs = [(0,0), (10,0), (0,10), (10,10)]

def get_dist(x1:float, x2:float, y1:float, y2:float) -> float:
    """
    Finds distance 
    between two points
    """
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return dist


def avg_dist(points:list) -> float:
    """
    Finds the average distance between 
    points in a list of tuples
    """
    total_dist = 0
    if_state_count = 0

    for i in range(len(points)):
        point = points[i]
        x1 = point[0]
        y1 = point[1]
        for j in range(len(points)):
            if j > i:
                point2 = points[j]
                x2 = point2[0]
                y2 = point2[1]
                total_dist += get_dist(x1, x2, y1, y2)
                if_state_count += 1
    return total_dist/if_state_count

print(avg_dist(xs))