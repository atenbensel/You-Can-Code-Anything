def is_palindrome(word):
    """
    Check if a word is a palindrome.
    """
    # Convert the word to lowercase and remove non-alphanumeric characters
    word = ''.join(char.lower() for char in word if char.isalnum())
    # Compare the word with its reverse
    return word == word[::-1]

def main():
    print("Welcome to the Palindrome Checker!")
    word = input("Enter a word or phrase: ")
    if is_palindrome(word):
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome.")

if __name__ == "__main__":
    main()
