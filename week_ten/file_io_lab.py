# Reading in
# Module = python file Ex. something.py
# '\\' in file location because '\' is an escape character.
# '\\' makes a single non-escape slash in python and many other languages

# Relative path: file path is described from our current working 
# directories path
# '.' means current working directory
# '..' means up one directory

# v Opens the file and names it 'f'. 'f' is an iterable object,
# so we can 'for' loop over it. This gives us the file 
# line by line.

# with open('week_ten/myfile.txt') as f:
    # for line in f:
        # print(line.rstrip())

# 'rstrip()' stands for right strip. Stripping all whitespace,
# including newline characters from the right of the string
# otherwise you get a big gap inbetween print statements

# > Writing Files with Open

# with open('week_ten/textFile3.txt','w') as file: # 'w' means you intend to write in the file
#     file.write('Hello this is a test\n')
#     file.write('File 3 IO!')

# > 1 - Total number of words in text file

f = open("week_ten/twocities_lab.txt", "r")

txtFile = f.read()
twoCities = txtFile.split()
word_count = len(twoCities)
print(word_count) # prints number of words

# 2 > Number of distinct words

distinct_words =[]
for word in twoCities:
    if word not in distinct_words:
        distinct_words.append(word)
# print(distinct_words) # make sure it was separating by word
# print(len(distinct_words))

# > 3 The longest word and its length

lengthiest_word = twoCities[0]
for word in twoCities:
    if len(word) > len(lengthiest_word):
        lengthiest_word = word
print(lengthiest_word) # the longest word as iterated above
print(len(lengthiest_word)) # length of the longest word

# > 4 Distinct words sorted by length

# print(sorted(distinct_words, key = len, reverse = True)) # sorts longest to shortest
# print(sorted(distinct_words, key = len)) # sorts shorteset to longest

# > 5 Most common word

word_counter = {}
for word in twoCities:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

common_word = list(word_counter.keys())[0]
for k, v in word_counter.items():
    if v > word_counter[common_word]:
        common_word = k

print(common_word) # prints the most common word (the)

# > 6 Words and their frequency sorted by frequency
word_freq = {k: v for k,v in sorted(word_counter.items(), key = lambda item: item[1])} # can add 'reverse = True' for longest to shortest

print(word_freq)

# > 7 Punctuation ?

f.close()