# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word.
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!
import numpy as np

words = np.array(["Hello","world","I´m", "Rolli"])

def smash(words):
    space= " "
    concat = words[0]
    for i in range (1 , len(words), 1):
      concat = concat + space + words[i]

    return concat

print("La cadena es la siguiente: " ,smash(words))