"""Write a python program that checks if two strings are anagrams of each 
other. """
string1 = "listen"
string2 = "silent"

string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

char_frequency1 = {}
char_frequency2 = {}

for char in string1:
    if char in char_frequency1:
        char_frequency1[char] += 1
    else:
        char_frequency1[char] = 1

for char in string2:
    if char in char_frequency2:
        char_frequency2[char] += 1
    else:
        char_frequency2[char] = 1

are_anagrams = char_frequency1 == char_frequency2

if are_anagrams:
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
