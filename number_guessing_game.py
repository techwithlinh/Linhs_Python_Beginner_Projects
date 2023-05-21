import random

while True:
    welcome = "Welcome to the random number guessing game. Please set a random range of numbers."
    print(welcome)
    input_number_1 = int(input("1st number: "))
    input_number_2 = int(input(f"2nd number (bigger than {input_number_1}): "))

    def check_numbers(input_number_1, input_number_2): 
        if input_number_2 <= input_number_1:
            print(f"Invalid value. Please enter a number that is bigger than {input_number_1}")
            return False
        return True

    isValid = check_numbers(input_number_1, input_number_2)
    if isValid:
        random_number = random.randint(input_number_1, input_number_2)
        print(f"\nThe random number is {random_number}")
        
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'n':
        break
        
print("\nThanks for playing!")
