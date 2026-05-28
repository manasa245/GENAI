# Function to check if a word is a palindrome


def is_palindrome(word):
    cleaned_word = word.lower()
    reversed_word = cleaned_word[::-1]
    return cleaned_word == reversed_word

test_word = "MOM"

if is_palindrome(test_word):
    print(f"Yes, '{test_word}' is a palindrome!")
else:
    print(f"No, '{test_word}' is not a palindrome.")