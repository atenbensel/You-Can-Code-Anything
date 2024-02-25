import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 100. Try to guess it.")

# Main game loop
while True:
    # Prompt the user to guess the number
    guess = int(input("Enter your guess: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number correctly!")
        break
    elif guess < secret_number:
        print("Too low! Try guessing a higher number.")
    else:
        print("Too high! Try guessing a lower number.")
