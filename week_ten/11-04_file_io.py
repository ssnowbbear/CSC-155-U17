absolute_path = "/home/noah/school_repos/CSC-155-U17/CSC-155-U17/week_ten/info.txt"
relative_path = "week_ten/info.txt"

#relative_path is better to use than absolute path, easier for others to read
#absolute_path is a security risk and you "look like a noob," words of my instructor
# Instructor for president "You'll look like a total noob" -Instructor approved message
#Instructor says, "I will grumble about absolute paths but I'll forgive it"
#"Later on I expect you to use relative_path"

with open('week_ten/info.txt') as f:
    for line in f:
        # line is a string, we can do string stuff with it
        print(line.rstrip())
        print(line.lower())
        print(line.upper())
        # print each word on a separate line
        words = line.split()
        for w in words:
            print(w)

#write a new file
with open('week_ten/info2.txt','w') as file:
    file.write('Hello this is a test')
    file.write('\nFile IO') #will completely write over the file if there is anything
    #in the file before the 'write' function

