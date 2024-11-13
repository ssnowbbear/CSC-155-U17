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

# with open('week_ten/textFile3.txt','w') as file:
#     file.write('Hello this is a test\n')
#     file.write('File 3 IO!')

with open('twocities.txt', encoding = 'utf-8') as f:
    print('t')