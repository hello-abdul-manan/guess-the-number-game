import random

print('\nNumber Guessing Game!')

attempts_done = 0
attempts_left = 5

while True:
    try:
        # Get min and max range from user
        min_num = int(input('Enter the minimum number for the range: '))
        max_num = int(input('Enter the maximum number for the range: '))

        # Generate a secret number between user defined range
        secret_number = random.randint(min_num, max_num)
        break
    except ValueError:
        print('Please enter valid numbers.')

while True:
    # Check if user has attempts
    if attempts_left == 0:
        print("You're out of attempts! Game over.")
        break

    try:
        # Show remaining attempts and get user guess
        print(f'You only have {attempts_left} attempts.')
        guess = int(input(f'Guess a number between {min_num} and {max_num}: '))

        # Compare user guess with secret number
        if guess > secret_number:
            attempts_done += 1
            attempts_left -= 1
            print('Too High! Try again.')
        elif guess < secret_number:
            attempts_done += 1
            attempts_left -= 1
            print('Too Low! Try again.')
        else:
            attempts_done += 1
            print(f'Congratulations! You guessed the number in {attempts_done} attempts.')
            break

    except ValueError:
        print('Please enter a valid number.')
