#-------------LOOK ONLINE FOR DICTIONARY CODE------------------

mySet = {'a', 4, 'dog', 8.5}
print(mySet)
#cannot change value in a set without taking a value out directly, does not allow duplicates
#sets do not have guaranteed order

mySet.add('a')
print(mySet)

mySet.remove('a')
print(mySet)
#can remove things

mySet.update({'a', 7, 'taco', 'cat', 9})
print(mySet)
#does not allow duplicates

#count unique characters in a sentence
#get a sentence from the user
sentence = input('Please enter a sentence: ')
#put each character into a set
char_set = set()
    #loop through all characters in the sentence
for i in range(len(sentence)):
    char_set.add(sentence[i])
#print how many characters are in the set
print(len(char_set))