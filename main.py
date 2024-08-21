import random
import string

def generatePassword(min_length, numbers, special_char):
    letters = string.ascii_letters
    digits = string.digits
    specialChar = string.punctuation

    if numbers and special_char:
        allChar = letters + digits + specialChar
    if not numbers and not special_char:
        allChar = letters
    if numbers and not special_char:
        allChar = letters + digits
    if not numbers and special_char:
        allChar = letters + specialChar

    password = ""
    
    for i in range(min_length):
        randomChar = random.choice(allChar)
        password += randomChar
    
    print(password)

def validInput(prompt):
    while True:
        response = input(prompt).lower()
        if response in ['y', 'n']:
            return response == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def validLength(prompt):
    while True:
        try:
            response = int(input(prompt))
            if response > 0:
                return response
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


min_length = validLength("Enter the password length: ")
has_numbers = validInput("Do you want numbers (y/n): ")
has_specialChar = validInput("Do you want special characters (y/n): ")
generatePassword(min_length, has_numbers, has_specialChar)

