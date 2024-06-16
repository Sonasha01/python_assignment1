"""Write a program that asks the user for their birth year and calculates their 
age. """


birth_year = int(input("Please enter your birth year: "))
current_year = 2024  
age = current_year - birth_year
print("You are", age, "years old.")
