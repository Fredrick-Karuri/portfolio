
##### Dictionaries (Hash Maps) ######

# This is the secret weapon for O(1) lookups
char_count ={}

#Adding items
char_count['a'] = 1
char_count['b'] = 2
print("Dict:",char_count)

# Safe lookup with .get() - returns None if key does not exist
print("Value of 'a': ",char_count.get('a'))
print("Value of 'z': ",char_count.get('z')) #Return None
print ("Value of 'z' with default: ", char_count.get('z',0)) #return 0

#Checking if key exists
if 'a' in char_count:
    print(" 'a' is in the dictionary. ")

# Iterating through a dictionary
for key, value in char_count.items():
    print(f"Key:{key}, Value: {value}")

# Common pattern : counting frequency
'''
# Pseudocode
repeat for every character:
    current_count = existing_count if any, otherwise 0
    new_count = current_count + 1
    store new_count in dictionary under that character

'''

text = "hello"
freq = {}
for char in text:
    current_count = freq.get(char,0) # get its current count
    new_count= current_count + 1 # add one
    freq[char] = new_count # store the updated count

print("Character frequency:", freq)

# using counter from collections
from collections import Counter
freq = Counter(text)
print("Using Counter: ", freq)



# function that counts how many times each word appears in a sentence
def count_words(sentence):
    """
    how to do it :
    1.split the sentence into individual words
    2.create an empty dict
    3.loop through each word
    4.if the word is already in the dictionary increase its count
    5.if its new add it with a count of 1 
    """
    sentence_words = sentence.split()
    seen_words={}

    for word in sentence_words:
        if word in seen_words:
            seen_words[word] += 1 # increase the count
        else:
            seen_words[word] =1 # first time seeing it 
            
    return seen_words

print("Word count:",count_words("hello world hello"))
