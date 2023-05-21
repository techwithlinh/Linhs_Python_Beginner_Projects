import random
import string

def generate_password(length):
    """This function generates a random password of given length"""
    # Define the pool of characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation

    # Use random.sample to ensure each character is unique
    password = random.sample(chars, length)

    # Join the characters into a string
    password = ''.join(password)

    return password

while True:
    user_input = input("\nEnter the new password's length (or 'exit' to quit): ")
    
    if user_input == 'exit':
        break

    try:
        user_input = int(user_input)
        
        if user_input <= 0:
            raise ValueError('\nPassword length must be greater than zero. Please try again')
        
        password = generate_password(user_input)
        print("\nYour new password is: "+password)

        save_choice = input("Would you like to save this password? (y/n): ")
        
        if save_choice.lower() == 'y':
            file_name = input("Enter a file name for your password: ")
            with open(file_name, 'w') as file:
                file.write(password)
                print("Password saved to file: "+file_name)
        
    except ValueError as e:
        print("\nInvalid input: ", e, "Please try again!")
        continue