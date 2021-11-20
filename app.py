# Create welcome message that asks to create account and takes user input

print("Welcome! Please create an account:")

userName = input("Please enter username: ")
passWord = input("Please enter password: ")

# Print a congratulations message and ask user to log in

print("Congratulations! You have created a new account.")
print("Please log in:")

# Ask for user input and check if it matches the login credentials, if yes print a scucces message if not print a invalid credential message

userNameInput = input("Please enter your user name: ")
passWordInput = input("Plese enter your password: ")

if userNameInput == userName and passWordInput == passWord:
    print("Welcome! You have successifully logged in.")
else:
    print("Sorry! You have entered invalid credentials.")
