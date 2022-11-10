# Given:
# sentence = "This is a common interview question, you can try it out."
# find the most repeated character in a text (spaces not included)

# Solution
# find How many times a character is repeated
# which atat structure --> dictionary
# character as key, repetions (frequency) as value

sentence = "This is a common interview question, you can try it out."

char_freq = {} # Created a dictionary

# iterate over the strings and get character and frequencey into the dictionary
for char in sentence.lower():
    if(char != ' '): # with this line, we removed the spaces
        if(char in char_freq):
            char_freq[char] += 1
        else:
            char_freq[char] = 1
#print(char_freq)

# step: sort the dictionary by frequency of characters
# Since we cannot sort dictionary, we covert to a list of tuples which we can sort

#for key in char_freq:
#    print(key)

#for key in char_freq:
#    print(key, char_freq)

#for item in char_freq.items():
#    print(item)

# sorted(char_freq.items())

#print(sorted(char_freq.items(), key=lambda kv:kv[1], reverse=True))

char_freq_sorted = sorted(char_freq.items(), key=lambda kv:kv[1], reverse=True)
print(char_freq_sorted[0][0])


