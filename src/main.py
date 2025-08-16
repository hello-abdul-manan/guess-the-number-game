import random

# Generate a secret number between 1 and 50
secret_number = random.randint(1, 50)

print('\nWelcome to the Number Guessing Game!')
print('Guess a number between 1 and 50.')

while True:
    # Get user guess
    guess = int(input('Enter your guess: '))

    # Compare guess with user secret number
    if guess == secret_number:
        print('Congratulations! You guessed the correct number.')
        break
    elif guess < secret_number:
        print('Too Low! Try again.')
    else:
        print('Too High! Try again.')
