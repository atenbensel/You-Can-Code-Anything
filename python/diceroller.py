import random

def roll_dice():
    """
    Simulate rolling a six-sided dice.
    """
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Roller!")

    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled: {result}")

        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for using the Dice Roller. Goodbye!")

if __name__ == "__main__":
    main()
