"""Write a program in python that counts the frequency of each character in 
a string. """
input_string = "hello world"
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print("Character frequencies:")
for char in char_frequency:
    print(f"'{char}': {char_frequency[char]}")
