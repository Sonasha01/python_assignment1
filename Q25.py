
#Write a program that copies the contents of one text file to another.
source_file = 'source.txt'
destination_file = 'destination.txt'

try:
    
    with open("C:/Users/SOSA/OneDrive/jobb/python_assignment1/output.txt", 'r') as src:
        content = src.read()

    with open("C:/Users/SOSA/OneDrive/jobb/python_assignment1/output2.txt", 'w') as dest:
        dest.write(content)

    print(f"Content copied from {source_file} to {destination_file} successfully.")
except FileNotFoundError:
    print(f"The file {source_file} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")