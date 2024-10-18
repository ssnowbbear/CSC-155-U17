# > 1 Program that counts vowels in a user inputted line.

user_line = str(input("Enter a line: ")).lower() #takes an input from the user and lower cases it

vowels = ["a", "e", "i", "o", "u"] #list of vowels

vowel_count = 0 #keeps track of vowels in 

for letter in range(len(user_line)): #loops through sentence
    if user_line[letter] in vowels: #looks if letter in user_line is in list of vowels
        vowel_count += 1 #increases vowel count

print(f"Vowels used in your sentence: {vowel_count}")

