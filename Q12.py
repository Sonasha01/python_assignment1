"""Write a python program that calculates the sum of the digits of a given 
number. """

number = 12345
number_str = str(number)
sum_of_digits = 0
for digit in number_str:
    sum_of_digits += int(digit)
print("The sum of the digits of", number, "is", sum_of_digits)
