"""Write a program in python that converts a given string to title case (first 
letter of each word capitalized). """


input_string = "hello world! this is a test."
words = input_string.split()
title_cased_words = []

for word in words:
   
    if len(word) > 0:
        title_cased_word = word[0].upper() + word[1:].lower()
        title_cased_words.append(title_cased_word)

title_cased_string = " ".join(title_cased_words)

print("Original String:", input_string)
print("Title Cased String:", title_cased_string)
