# Write a program to accept a string from the user and 
#display characters that are present at an even index number.

# Pseudocode

# User's input name
user_input = input("Please enter your complete name: ")

#Print name
print(user_input)

# Create a loop for even indices
for names in range (0, len(user_input), 2):

    # Print characters and index  even values
    print("Index Characters: ", user_input[names], "Index Values: ", [names])
    
