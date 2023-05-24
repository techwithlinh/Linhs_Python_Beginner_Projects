import random

while True:
    # List of words to choose from
    words = ["apple", "banana", "orange", "pear", "grape", "pineapple", "watermelon", "peach", "plum", "cherry", "raspberry", "blueberry"]

    # Select a random word
    word = random.choice(words)

    # Create a set of the word's letters
    word_letters = set(word)

    # Create a set of the player's guessed letters
    guessed_letters = set()

    # Set the number of tries the player starts with
    tries = 6

    # Loop until the player wins or loses
    while tries > 0:

        # Display the current state of the word
        print("Word:", end=" ")
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

        # Get the player's guess and validate it
        guess = input("Guess a letter: ").lower().strip()
        if guess == "exit":
            break
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add the guess to the guessed letters and decrement the tries if it's wrong
        guessed_letters.add(guess)
        if guess not in word_letters:
            tries -= 1

        # Check if the player has won or lost
        if word_letters.issubset(guessed_letters):
            print("Congratulations! You guessed the word: ", word)
            break
        else:
            print("Tries left:", tries)

    # If the player has no more tries left, they lose
    if tries == 0:
        print("Sorry, you lose. The word was: ", word)

    play_again = input("Would you like to play again? (y/n) ").strip().lower()
    if play_again != "y":
        break
