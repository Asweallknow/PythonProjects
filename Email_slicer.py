# Get user input for their email address and remove any leading or trailing whitespace
email = input("Enter your Email: ").strip()

# Extract the username part of the email (before the @ symbol)
username = email[:email.index("@")]

# Extract the domain name part of the email (after the @ symbol)
domain_name = email[email.index("@")+1:]

# Create a formatted string to display the extracted username and domain name
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")

# Print the formatted string to provide user information
print(format_)
