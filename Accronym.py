# Prompt the user to input a phrase
user_input = str(input("Enter a Phrase: "))

# Split the input phrase into a list of words
text = user_input.split()

# Initialize an empty string 'a' to store the uppercase initials
a = " "

# Iterate through each word in the 'text' list
for i in text:
    # Add the uppercase initial of the current word to the string 'a'
    a = a + str(i[0]).upper()

# Print the final string containing uppercase initials
print(a)
