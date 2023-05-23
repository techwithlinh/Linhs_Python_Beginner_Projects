import random

print("Let's play Rock Paper Scissors!")

choices = ["rock", "paper", "scissors"] # list of possible choices

while True:
    computer_choice = random.choice(choices) # computer chooses at random
    user_choice = input("Choose rock, paper, or scissors (or type 'no' to quit): ").lower() # get user choice and convert to lowercase
    
    if user_choice == "no":
        print("Thanks for playing!")
        break
    
    if user_choice not in choices:
        print("Invalid input. Please try again.")
        continue
    
    print("Computer chose:", computer_choice)

    # check who wins
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" and computer_choice == "rock" or user_choice == "scissors" and computer_choice == "paper":
        print("You win!") #rock beats scissors - paper beats rock - scissors beats paper
    else:
        print("You lose!")
