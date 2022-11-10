# Given:
# sentence = "This is a common interview question, you can try it out."
# find the most repeated character in a text (spaces not included)

# Solution
# find How many times a character is repeated
# which atat structure --> dictionary
# character as key, repetions (frequency) as value

sentence = "This is a common interview question, you can try it out."

char_freq = {}

# iterate over the strings and get character and frequencey into the dictionary
for char in sentence:
    if(char in char_freq):
        char_freq[char] += 1
    else:
        char_freq[char] = 1
print(char_freq)