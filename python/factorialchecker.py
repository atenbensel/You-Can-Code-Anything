def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("Welcome to the Factorial Calculator!")
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Error: Please enter a non-negative integer.")
            else:
                print(f"The factorial of {num} is {factorial(num)}.")
                break
        except ValueError:
            print("Error: Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()
