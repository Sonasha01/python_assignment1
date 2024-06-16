#5. Write a program that takes a string input from the user and writes it to a text file

user_input = input("Enter a string: ")
with open("C:/Users/Dell/Downloads/IGDTUW ph &Ml/Ass. Q5.txt", "w") as file:
    file.write(user_input)

print("The string has been written to output.txt")
